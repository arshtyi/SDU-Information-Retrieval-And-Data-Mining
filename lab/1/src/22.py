def model_fit_quality(training_accuracy, test_accuracy):
    """
    基于训练和测试准确率,确定模型是否过拟合、欠拟合或拟合良好，返回1、-1、0。
    :param training_accuracy: float, 训练准确率 (0 <= training_accuracy <= 1)
    :param test_accuracy: float, 测试准确率 (0 <= test_accuracy <= 1)
    :return: int, 1、-1、0
    """
    return -1 if training_accuracy < 0.7 and test_accuracy < 0.7 else (1 if training_accuracy - test_accuracy > 0.2 else 0)


if __name__ == "__main__":
    training_accuracy, test_accuracy = map(float, input().split())
    print(model_fit_quality(training_accuracy, test_accuracy))
