import "./styles.css";

function chocolateFeast(n, c, m) {
  // Write your code here
  let ch = Math.floor(n / c);
  let wr = ch;
  let ch_temp = ch;
  while (wr >= m) {
    ch_temp = Math.floor(wr / m);
    wr = (wr % m) + ch_temp;
    ch += ch_temp;
  }
  return ch;
}

//chocolateFeast(15, 3, 2);

document.getElementById("app").innerHTML = `
<h1>${chocolateFeast(19, 3, 8)}</h1>
`;
