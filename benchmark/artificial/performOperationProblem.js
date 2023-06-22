function performOperation(expression) {
    var parts = expression.split(" ");
    var operand1 = parseInt(parts[0]);
    var operator = parts[1];
    var operand2 = parseInt(parts[2]);
    
    var result;
    
    switch (operator) {
      case '+':
        result = operand1 + operand2;
        break;
      case '-':
        result = operand1 - operand2;
        break;
      case '*':
        result = operand1 * operand2;
        break;
      case '/':
        result = operand1 / operand2;
        break;
      default:
        throw new Error("Invalid operator: " + operator);
    }
    
    return result;
  }

  module.exports = performOperation