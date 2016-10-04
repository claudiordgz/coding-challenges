#include <cmath>
#include <cstdio>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;

/* Retrieves a string until certain condition is met
 * Changes i
 */
std::string getElement(int (*comparison)(int), std::size_t &i, std::string const& expression) {
  auto letter = expression.at(i);
  std::string to_push;
  while((*comparison)(letter) > 0) {
    to_push += letter;
    i += 1;
    if(i >= expression.length()) {
      break;
    }
    letter = expression.at(i);
  }
  return to_push;
}


#define MOD 1000000007

long long int superpower (long long int a, long long int b) {
  long long int ans=1ll;
  while(b) {
    if(b&1)ans=(ans*a)%MOD;
    a=(a*a)%MOD;
    b=b/2;
  }
  return ans;
}

int isnotdigit(char c) {
  return c == '*' ? 1 : 0;
}

enum class States {multiply,power,none};

States processOperator(int n) {
  switch (n) {
    case 1:
      return States::multiply;
    case 2:
      return States::power;
    default:
      return States::none;
  }
}

std::string eval(std::string const &expression) {
  if (expression.empty() || expression.at(0) == '*' || expression.at(expression.length() - 1) == '*') {
    return "Syntax Error";
  } else {
    States states = States::none;
    std::stack<long long int> numbers;
    std::size_t i = 0;
    while(i < expression.length()) {
      auto c = expression.at(i);
      if(std::isdigit(c)) {
        if(c == '0') {
          return "Syntax Error";
        }
        long long int latestNumber = std::stoull(getElement(std::isdigit, i, expression));
        // Checks
        if (states == States::power) {
          long long int previous = numbers.top();
          numbers.pop();
          numbers.push(superpower(previous, latestNumber));
        } else {
          numbers.push(latestNumber);
        }
      } else {
        std::string opStr = getElement(std::ispunct, i, expression);
        auto op = opStr.length();
        states = processOperator(op);
        if(states == States::none) return "Syntax Error";
      }
    }
    long long int acc = numbers.top();
    numbers.pop();
    while (!numbers.empty())
    {
       acc *= numbers.top();
       numbers.pop();
    }
    std::cout << acc << std::endl;
    return std::to_string(acc);
  }
}

int main() {
  std::string n;
  std::getline(std::cin, n);

  for (std::string line; std::getline(std::cin, line);) {
    std::cout << eval(line) << std::endl;
  }

  return 0;
}
