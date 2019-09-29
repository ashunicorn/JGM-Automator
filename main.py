from automator import Automator
from target import TargetType

if __name__ == '__main__':
    # 声明货物要移动到的建筑 ID 。
    targets = {
        TargetType.Chair: 3,
        TargetType.Wood: 9,
        TargetType.Bottle: 4,
        TargetType.Bag: 5,
        TargetType.Box: 2,
        TargetType.Grass: 8,
        TargetType.Sofa: 1,
        TargetType.Iron: 7,
        TargetType.Book: 6
    }

    # 连接 adb 。
    instance = Automator('127.0.0.1:7555', targets)

    # 启动脚本。
    instance.start()
