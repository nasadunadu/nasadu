"""
Trae core module
核心模块
"""


class Trae:
    """
    Trae main class
    Trae 主类
    """

    def __init__(self, name: str = "Trae"):
        """
        Initialize Trae instance
        初始化 Trae 实例

        Args:
            name: Name of the instance (实例名称)
        """
        self.name = name

    def run(self) -> str:
        """
        Run the main function
        运行主函数

        Returns:
            str: Greeting message (问候消息)
        """
        return f"Hello from {self.name}!"

    def process(self, data: str) -> str:
        """
        Process input data
        处理输入数据

        Args:
            data: Input data to process (待处理的输入数据)

        Returns:
            str: Processed result (处理结果)
        """
        return f"[{self.name}] Processed: {data}"
