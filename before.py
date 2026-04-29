"""
包含明显坏味道的代码 - 两个几乎完全相同的函数
CodeQL 一定能检测到重复代码问题
"""

def get_student_info(name, student_id, grade, school):
    """获取学生信息并格式化输出"""
    
    # 验证输入
    if name is None or name == "":
        print("错误：学生姓名不能为空")
        return None
    if student_id is None or student_id == "":
        print("错误：学号不能为空")
        return None
    if grade <= 0 or grade > 12:
        print("错误：年级必须在1-12之间")
        return None
    if school is None or school == "":
        print("错误：学校名称不能为空")
        return None
    
    # 处理学生信息
    student_name_upper = name.upper()
    student_id_clean = student_id.strip()
    
    # 生成学生报告
    print("=" * 50)
    print("学生信息报告")
    print("=" * 50)
    print(f"学生姓名: {student_name_upper}")
    print(f"学号: {student_id_clean}")
    print(f"年级: {grade}年级")
    print(f"学校: {school}")
    print("-" * 50)
    print(f"信息完整度: 100%")
    print("=" * 50)
    
    return {
        "name": student_name_upper,
        "student_id": student_id_clean,
        "grade": grade,
        "school": school
    }


def get_teacher_info(name, teacher_id, department, school):
    """获取教师信息并格式化输出"""
    
    # 验证输入（与上面几乎相同的逻辑）
    if name is None or name == "":
        print("错误：教师姓名不能为空")
        return None
    if teacher_id is None or teacher_id == "":
        print("错误：工号不能为空")
        return None
    if department is None or department == "":
        print("错误：部门名称不能为空")
        return None
    if school is None or school == "":
        print("错误：学校名称不能为空")
        return None
    
    # 处理教师信息
    teacher_name_upper = name.upper()
    teacher_id_clean = teacher_id.strip()
    
    # 生成教师报告
    print("=" * 50)
    print("教师信息报告")
    print("=" * 50)
    print(f"教师姓名: {teacher_name_upper}")
    print(f"工号: {teacher_id_clean}")
    print(f"部门: {department}")
    print(f"学校: {school}")
    print("-" * 50)
    print(f"信息完整度: 100%")
    print("=" * 50)
    
    return {
        "name": teacher_name_upper,
        "teacher_id": teacher_id_clean,
        "department": department,
        "school": school
    }


def get_course_info(course_name, course_code, credit, teacher):
    """获取课程信息并格式化输出"""
    
    # 验证输入（又是完全相同的验证模式）
    if course_name is None or course_name == "":
        print("错误：课程名称不能为空")
        return None
    if course_code is None or course_code == "":
        print("错误：课程代码不能为空")
        return None
    if credit <= 0 or credit > 10:
        print("错误：学分必须在1-10之间")
        return None
    if teacher is None or teacher == "":
        print("错误：任课教师不能为空")
        return None
    
    # 处理课程信息
    course_name_upper = course_name.upper()
    course_code_clean = course_code.strip()
    
    # 生成课程报告
    print("=" * 50)
    print("课程信息报告")
    print("=" * 50)
    print(f"课程名称: {course_name_upper}")
    print(f"课程代码: {course_code_clean}")
    print(f"学分: {credit}")
    print(f"任课教师: {teacher}")
    print("-" * 50)
    print(f"信息完整度: 100%")
    print("=" * 50)
    
    return {
        "course_name": course_name_upper,
        "course_code": course_code_clean,
        "credit": credit,
        "teacher": teacher
    }


# 测试代码
if __name__ == "__main__":
    print("\n测试学生信息:")
    print(get_student_info("张三", "2024001", 10, "第一中学"))
    
    print("\n测试教师信息:")
    print(get_teacher_info("李老师", "T001", "计算机系", "第一中学"))
    
    print("\n测试课程信息:")
    print(get_course_info("Python编程", "CS101", 3, "李老师"))
