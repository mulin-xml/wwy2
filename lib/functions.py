import cv2


class CircleCounter():
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.circles = []

        # 手动信号槽
        self.ui.pushButton_2.clicked.connect(self.calc)

    def render_img(self):
        img = self.img.copy()
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # 灰度图
        for i in self.circles:  # 遍历矩阵的每一行的数据
            img = cv2.circle(img, (int(i[0]), int(i[1])), int(i[2]), (255, 255, 0), 1)
            img = cv2.circle(img, (int(i[0]), int(i[1])), 1, (255, 255, 0), -1)
        self.imshow(img)
        return super().render_img()

    def calc(self):
        self.printf('计算中 大约耗时几秒 请耐心等待')
        self.circles = cv2.HoughCircles(self.img.squeeze(), cv2.HOUGH_GRADIENT, 1, 40, param1=50, param2=20, minRadius=0, maxRadius=100).squeeze()
        self.printf(self.circles)
        self.render_img()
