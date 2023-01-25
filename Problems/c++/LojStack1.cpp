#include <iostream>
#include <stack>

using namespace std;

int main(int argc, char *argv[]) {
  int t;

  cin >> t;
  getchar(); // apparently reads the newline after test case
  for (int i = 0; i < t; i++) {
    cout << "Case " << i+1 << ":\n";
    string query, url;
    // new url goes in the forward stack
    // when forward is empty then return ignored
    // every forward query pops from forward and pushes to back
    // every back query pops from back and pushes to forward
    // every visit query pops forward and pushes back,
    // empties forward and makes the visit link the top of forward
    stack<string> forwardStack, backStack;
    forwardStack.push("http://www.lightoj.com/");
    while (1) {
      cin >> query;
      string temp;
      if(query == "VISIT") {
        cin >> url;
        if(!forwardStack.empty()) {
          temp = forwardStack.top();
          backStack.push(temp);
          while(!forwardStack.empty()) {
            forwardStack.pop();
          }
          forwardStack.push(url);
          cout << forwardStack.top() << "\n";
        }
      }
      else if(query == "BACK") {
        if(backStack.empty()) {
          cout << "Ignored" << "\n";
        } else {
          temp = backStack.top();
          backStack.pop();
          forwardStack.push(temp);
          cout << forwardStack.top() << "\n";
        }
      }
      else if(query == "FORWARD") {
        if(forwardStack.size() < 2) {
          cout << "Ignored" << "\n";
        } else {
          temp = forwardStack.top();
          forwardStack.pop();
          backStack.push(temp);
          cout << forwardStack.top() << "\n";
        }
      }
      else if(query == "QUIT") {
        break;
      }
    }
  }

  return 0;
}
