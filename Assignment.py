import random
import json

def main():
    size = random.randint(3, 5)

    factors = []
    if size == 3:
        factor1 = random.choice([2, 3, 5, 7, 11, 13])
        number = factor1 * factor1
        factors.append(factor1)
    elif size == 4:
        factor1 = random.choice([2, 3, 5])
        factor2 = random.choice([7, 11, 13])
        number = factor1 * factor2
        factors.extend([factor1, factor2])
    elif size == 5:
        factor1 = random.choice([2, 3, 5])
        factor2 = random.choice([7, 11, 13])
        factor3 = random.choice([2, 3, 5])
        while factor3 == factor1:
            factor3 = random.choice([2, 3, 5])
        number = factor1 * factor2 * factor3
        factors.extend([factor1, factor2, factor3])

    factors.sort()
    all_factors = [1] + factors + [number]
    mean_ = sum(all_factors) / len(all_factors)

    # Check if mean is an integer
    if mean_.is_integer():
        mean = int(mean_)
    else:
        mean = round(mean_, 1)

    # Convert factors to LaTeX-compatible strings
    factors_latex1 = ", ".join(map(str, factors))
    factors_latex2 = " + ".join(map(str, all_factors))

    # Generate LaTeX question and answer
    q_tex = rf"""$$\text{{Find the mean of all the factors of }}{number}.$$

\[\text{{Note: Round off the answer to one decimal place.}}\]"""

    a_tex = rf"""$$\text{{We know that factors of }}{number}\text{{ are }}1, {factors_latex1}, \text{{ and }}{number}.$$

$$\text{{Arithmetic mean of all factors of }}{number}$$

$$ = \frac{{{factors_latex2}}}{{{len(all_factors)}}}$$

$$ = \frac{{{sum(all_factors)}}}{{{len(all_factors)}}}$$

$$ = {mean}$$"""

    # Output result as JSON
    result = {
        "q_tex": q_tex,
        "a_tex": a_tex
    }

    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()