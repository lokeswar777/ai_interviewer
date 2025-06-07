from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from typing import List, Dict, Any
import asyncio

class LLMService:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.max_length = 2048
        self.initialized = False

    async def initialize(self):
        """Initialize the LLM model and tokenizer"""
        if not self.initialized:
            try:
                # Load Llama model and tokenizer
                model_name = "meta-llama/Llama-2-7b-hf"  # You'll need appropriate credentials
                self.tokenizer = AutoTokenizer.from_pretrained(model_name)
                self.model = AutoModelForCausalLM.from_pretrained(
                    model_name,
                    torch_dtype=torch.float16,
                    device_map="auto"
                )
                self.initialized = True
                return True
            except Exception as e:
                print(f"Error initializing LLM: {str(e)}")
                return False

    async def generate_suggestions(self, code: str) -> List[str]:
        """
        Generate code suggestions based on the current code
        
        Args:
            code (str): The current code in the editor
            
        Returns:
            List of suggestion strings
        """
        if not self.initialized:
            await self.initialize()

        try:
            prompt = f"""Given this Python code:
            {code}
            
            Suggest improvements or completions for this code:"""

            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_length=self.max_length,
                    num_return_sequences=3,
                    temperature=0.7,
                    top_p=0.95,
                    do_sample=True
                )

            suggestions = [
                self.tokenizer.decode(output, skip_special_tokens=True)
                for output in outputs
            ]

            # Process and clean up suggestions
            cleaned_suggestions = [
                suggestion.replace(prompt, "").strip()
                for suggestion in suggestions
            ]

            return cleaned_suggestions

        except Exception as e:
            print(f"Error generating suggestions: {str(e)}")
            return []

    async def explain_code(self, code: str, detail_level: str = "medium") -> Dict[str, Any]:
        """
        Generate explanation for the given code
        
        Args:
            code (str): The code to explain
            detail_level (str): Level of detail for the explanation
            
        Returns:
            Dictionary containing explanation and any additional insights
        """
        if not self.initialized:
            await self.initialize()

        try:
            detail_prompts = {
                "basic": "Briefly explain what this code does:",
                "medium": "Explain what this code does and how it works:",
                "detailed": "Provide a detailed explanation of this code, including its purpose, implementation details, and potential improvements:"
            }

            prompt = f"""{detail_prompts.get(detail_level, detail_prompts["medium"])}
            
            {code}"""

            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_length=self.max_length,
                    temperature=0.7,
                    top_p=0.95,
                    do_sample=True
                )

            explanation = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            explanation = explanation.replace(prompt, "").strip()

            return {
                "explanation": explanation,
                "suggestions": await self.generate_suggestions(code)
            }

        except Exception as e:
            print(f"Error generating explanation: {str(e)}")
            return {
                "explanation": "Error generating explanation",
                "suggestions": []
            }

# Global instance
llm_service = LLMService()
