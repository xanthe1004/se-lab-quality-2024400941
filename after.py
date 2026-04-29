"""
修复后：完全消除所有 f-string 问题，提取重复逻辑
"""

def validate_input(value, field_name):
    """共享的验证函数"""
    if value is None or value == "":
        return False, "错误：" + field_name + "不能为空"
    return True, ""


def format_report(title, fields):
    """共享的格式化输出函数 - 不使用 f-string"""
    print("=" * 60)
    print(title)
    print("=" * 60)
    for key, value in fields.items():
        # 使用普通字符串拼接，完全避免 f-string
        print(key + ": " + str(value))
    print("-" * 60)
    print("信息完整度: 100%")
    print("数据状态: 已验证")
    print("=" * 60)


def process_student_data(name, student_id, grade, school):
    """处理学生数据"""
    
    # 验证
    valid, msg = validate_input(name, "姓名")
    if not valid:
        return msg
    valid, msg = validate_input(student_id, "学号")
    if not valid:
        return msg
    if grade <= 0:
        return "错误：年级必须大于0"
    valid, msg = validate_input(school, "学校")
    if not valid:
        return msg
    
    # 年级级别处理
    grade_level = ""
    if grade <= 6:
        grade_level = "小学"
    elif grade <= 9:
        grade_level = "初中"
    else:
        grade_level = "高中"
    
    # 格式化输出 - 不使用 f-string
    title = "学生信息报告"
    fields = {
        "姓名": name.strip().title(),
        "学号": student_id.strip().upper(),
        "年级": str(grade) + " (" + grade_level + ")",
        "学校": school.strip().title()
    }
    format_report(title, fields)
    
    return {"valid": True, "data": fields}


def process_teacher_data(name, teacher_id, department, school):
    """处理教师数据"""
    
    # 验证
    valid, msg = validate_input(name, "姓名")
    if not valid:
        return msg
    valid, msg = validate_input(teacher_id, "工号")
    if not valid:
        return msg
    valid, msg = validate_input(department, "部门")
    if not valid:
        return msg
    valid, msg = validate_input(school, "学校")
    if not valid:
        return msg
    
    # 格式化输出 - 不使用 f-string
    title = "教师信息报告"
    fields = {
        "姓名": name.strip().title(),
        "工号": teacher_id.strip().upper(),
        "部门": department.strip().title(),
        "学校": school.strip().title()
    }
    format_report(title, fields)
    
    return {"valid": True, "data": fields}


# 测试代码
if __name__ == "__main__":
    print("=" * 60)
    print("测试学生数据:")
    result1 = process_student_data("张三", "2024001", 10, "第一中学")
    print("返回结果:", result1.get("valid", False))
    
    print("\n" + "=" * 60)
    print("测试教师数据:")
    result2 = process_teacher_data("李老师", "T001", "计算机系", "第一中学")
    print("返回结果:", result2.get("valid", False))