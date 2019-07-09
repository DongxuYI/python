gl_list = [3, 5, 7, 1, 4, 2, 0, 8]

gl_list.sort(reverse=True)

# print(gl_list)


def gender_info(name, gender=True):
    gender_text = '男生'
    if not gender:
        gender_text = '女生'
    print(name, gender_text)


# gender_info('张三', False)


def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


demo(2, 3, 4, 5, name="YI")