import "./styles.css";

var num_strings = [
  "zero",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
  "ten",
  "eleven",
  "twelve",
  "thirteen",
  "fourteen",
  "fifteen",
  "sixteen",
  "seventeen",
  "eighteen",
  "ninteen"
];
var second_digit_string_prefixes = [
  null,
  null,
  "twenty",
  "thirty",
  "fourty",
  "fifty",
  "sixty",
  "seventy",
  "eighty",
  "ninety"
];

function getNumberString(n) {
  if (n >= 100) return "Does not support";
  if (n < num_strings.length) {
    return num_strings[n];
  }
  var s = second_digit_string_prefixes[Math.floor(n / 10)];
  if (n % 10 > 0) {
    s += " " + num_strings[n % 10];
  }
  return s;
}
const format_helper = {
  "0": (h) => `${getNumberString(h === 0 ? 12 : h)} o' clock`,
  "15": (h) => `quarter past ${getNumberString(h === 0 ? 12 : h)}`,
  "30": (h) => `half past ${getNumberString(h === 0 ? 12 : h)}`,
  "45": (h) => `quarter to ${getNumberString(h === 12 ? 1 : h + 1)}`,
  before_half: (h, m) =>
    `${getNumberString(m)} minute${m > 1 ? "s" : ""} past ${getNumberString(
      h === 0 ? 12 : h
    )}`,
  past_half: (h, m) =>
    `${getNumberString(60 - m)} minute${m > 1 ? "s" : ""} to ${getNumberString(
      h === 12 ? 1 : h + 1
    )}`
};
function timeInWords(h, m) {
  // Write your code here
  if (m % 15 === 0) {
    return format_helper[`${m}`](h);
  }
  if (m < 30) {
    return format_helper["before_half"](h, m);
  }
  if (m > 30) {
    return format_helper["past_half"](h, m);
  }

  return getNumberString(h);
}

timeInWords(21, 34);

document.getElementById("app").innerHTML = `
<h1>${timeInWords(43, 34)}</h1>
`;
