# 这是一个包含两个几乎相同函数的代码 - 存在重复代码坏味道

def calculate_rectangle_area(length, width):
    """计算矩形面积"""
    # 参数验证
    if length <= 0:
        print("错误：长度必须大于0")
        return None
    if width <= 0:
        print("错误：宽度必须大于0")
        return None
    
    # 计算面积
    area = length * width
    
    # 打印结果
    print(f"矩形的长是: {length}")
    print(f"矩形的宽是: {width}")
    print(f"矩形的面积是: {area}")
    
    # 额外信息
    if area > 100:
        print("这是一个大面积矩形")
    else:
        print("这是一个小面积矩形")
    
    return area


def calculate_square_area(side):
    """计算正方形面积"""
    # 参数验证
    if side <= 0:
        print("错误：边长必须大于0")
        return None
    
    # 计算面积
    area = side * side
    
    # 打印结果
    print(f"正方形的边长是: {side}")
    print(f"正方形的面积是: {area}")
    
    # 额外信息
    if area > 100:
        print("这是一个大面积正方形")
    else:
        print("这是一个小面积正方形")
    
    return area


# 测试代码
if __name__ == "__main__":
    print("=" * 30)
    print("测试矩形: 长5, 宽3")
    calculate_rectangle_area(5, 3)
    
    print("\n" + "=" * 30)
    print("测试正方形: 边长4")
    calculate_square_area(4)