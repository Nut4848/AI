from fractions import Fraction

def compute_probabilities(p_red, red_green, red_orange, blue_green, blue_orange):
    # จำนวนรวมในแต่ละกล่อง
    red_total = red_green + red_orange
    blue_total = blue_green + blue_orange

    # prior
    p_blue = 1 - p_red

    # conditional probabilities
    p_green_given_red = red_green / red_total if red_total>0 else 0
    p_orange_given_red = red_orange / red_total if red_total>0 else 0
    p_green_given_blue = blue_green / blue_total if blue_total>0 else 0
    p_orange_given_blue = blue_orange / blue_total if blue_total>0 else 0

    # marginal probabilities
    p_green = p_red * p_green_given_red + p_blue * p_green_given_blue
    p_orange = p_red * p_orange_given_red + p_blue * p_orange_given_blue

    # posterior P(Red | Orange)
    p_red_given_orange = 0
    if p_orange > 0:
        p_red_given_orange = (p_orange_given_red * p_red) / p_orange

    return {
        'red_total': red_total,
        'blue_total': blue_total,
        'p_green_given_red': p_green_given_red,
        'p_orange_given_red': p_orange_given_red,
        'p_green_given_blue': p_green_given_blue,
        'p_orange_given_blue': p_orange_given_blue,
        'p_green': p_green,
        'p_orange': p_orange,
        'p_red_given_orange': p_red_given_orange
    }


def nice_frac(x):
    try:
        return str(Fraction(x).limit_denominator())
    except Exception:
        return str(x)


def print_results(res):
    print("-- ข้อมูลในกล่อง --")
    print(f"Red total = {res['red_total']}, Blue total = {res['blue_total']}")
    print()
    print("-- ความน่าจะเป็นมีเงื่อนไข (conditional) --")
    print(f"P(Apple | Red)  = {nice_frac(res['p_green_given_red'])} = {res['p_green_given_red']:.4f}")
    print(f"P(Orange | Red) = {nice_frac(res['p_orange_given_red'])} = {res['p_orange_given_red']:.4f}")
    print(f"P(Apple | Blue) = {nice_frac(res['p_green_given_blue'])} = {res['p_green_given_blue']:.4f}")
    print(f"P(Orange | Blue)= {nice_frac(res['p_orange_given_blue'])} = {res['p_orange_given_blue']:.4f}")
    print()
    print("-- ความน่าจะเป็นรวม (marginal) --")
    print(f"P(Apple)  = {nice_frac(res['p_green'])} = {res['p_green']:.4f}")
    print(f"P(Orange) = {nice_frac(res['p_orange'])} = {res['p_orange']:.4f}")
    print()
    print("-- ความน่าจะเป็นแบบย้อนหลัง (posterior) --")
    print(f"P(Red | Orange) = {nice_frac(res['p_red_given_orange'])} = {res['p_red_given_orange']:.6f}")


if __name__ == '__main__':
    # ตัวอย่างจากรูปโจทย์:
    # กำหนดให้โอกาสหยิบกล่องแดง 40% และกล่องน้ำเงิน 60%
    # กล่องแดง มี Apple (สีเขียว) = 2 , Orange (สีส้ม) = 6  --> รวม 8
    # กล่องน้ำเงิน มี Apple = 3 , Orange = 1  --> รวม 4

    p_red = 0.40
    red_green = 2
    red_orange = 6
    blue_green = 3
    blue_orange = 1

    res = compute_probabilities(p_red, red_green, red_orange, blue_green, blue_orange)
    print_results(res)

    # ถ้าต้องการให้ผู้ใช้ป้อนค่าเอง ให้เอาคอมเมนต์ออกและเปิดส่วนด้านล่างนี้:
    # p_red = float(input('P(red) (ตัวอย่าง 0.4): '))
    # red_green = int(input('จำนวน Apple ในกล่องแดง: '))
    # red_orange = int(input('จำนวน Orange ในกล่องแดง: '))
    # blue_green = int(input('จำนวน Apple ในกล่องน้ำเงิน: '))
    # blue_orange = int(input('จำนวน Orange ในกล่องน้ำเงิน: '))
    # res = compute_probabilities(p_red, red_green, red_orange, blue_green, blue_orange)
    # print_results(res)
