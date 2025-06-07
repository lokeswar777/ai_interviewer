import subprocess
import tempfile
import os
import asyncio
from typing import Dict, Any
import time

class CodeExecutor:
    def __init__(self):
        self.timeout = 30  # Default timeout in seconds
        
    async def execute_python_code(self, code: str, timeout: int = None) -> Dict[str, Any]:
        """
        Execute Python code in a secure environment
        
        Args:
            code (str): Python code to execute
            timeout (int, optional): Execution timeout in seconds
            
        Returns:
            Dict containing execution results and metadata
        """
        if timeout:
            self.timeout = timeout

        try:
            # Create a temporary file to store the code
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                temp_file = f.name

            start_time = time.time()
            
            # Execute the code using subprocess with timeout
            try:
                result = subprocess.run(
                    ['python', temp_file],
                    capture_output=True,
                    text=True,
                    timeout=self.timeout,
                    cwd=tempfile.gettempdir()
                )
                
                execution_time = time.time() - start_time
                
                if result.returncode == 0:
                    return {
                        "status": "success",
                        "output": result.stdout,
                        "error": result.stderr if result.stderr else None,
                        "execution_time": execution_time
                    }
                else:
                    return {
                        "status": "error",
                        "output": result.stdout,
                        "error": result.stderr,
                        "execution_time": execution_time
                    }
                    
            except subprocess.TimeoutExpired:
                return {
                    "status": "timeout",
                    "output": None,
                    "error": f"Code execution timed out after {self.timeout} seconds",
                    "execution_time": self.timeout
                }
            finally:
                # Clean up temporary file
                try:
                    os.unlink(temp_file)
                except:
                    pass

        except Exception as e:
            return {
                "status": "error",
                "output": None,
                "error": f"Execution error: {str(e)}",
                "execution_time": 0.0
            }

# Global instance
code_executor = CodeExecutor()
