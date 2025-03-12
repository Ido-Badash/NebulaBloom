from pathlib import Path

class SafePath:
    def __init__(self, base_path: Path = None):
        if base_path:
            self._base_path = base_path
        else:
            self._base_path = Path.cwd()

    def get_base_path(self) -> Path:
        """Get the absolute path of the file"""
        return self._base_path
    
    def set_base_path(self, base_path: Path):
        """Set the absolute path of the file"""
        self._base_path = base_path

    def path(self, path: str, folder: str = "", as_string: bool = False) -> Path:
        """
        Get the path of the folder.
        Raises:
            FileNotFoundError: If the file is not found.
        """
        if not folder and not path or not path:
            raise FileNotFoundError(f"Path not found: {path} (Base path: {self._base_path}, Folder: {folder})")
        
        path = self._base_path / folder / path
        if not Path.exists(path):
            raise FileNotFoundError(f"Path not found: {path}")
        
        return path if not as_string else self._str_path(path)
    
    @staticmethod
    def _str_path(path: Path) -> str:
        """Get the string path of the file"""
        return path.as_posix()