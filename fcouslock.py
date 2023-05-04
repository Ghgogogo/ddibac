import time
from plyer import notification

count = 0
print("专注时钟已开始，开始工作吧！")

if __name__ == "__main__":
    while True:
        time.sleep(1800)
        count += 1
        notification.notify(
            title = "干得好！",
            message = "休息10分钟吧！你已经完成了" + str(count) + "个专注时钟",
        )
        time.sleep(600)
        notification.notify(
            title = "回到工作！",
            message = "再试着做一个专注时钟...",
        )
