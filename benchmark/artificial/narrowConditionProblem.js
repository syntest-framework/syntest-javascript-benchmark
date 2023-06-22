

function narrowConditionProblem(a, b, c) {

    if (a > 100) {
        if (a < 101) {
            if (b < 11) {
                if (b > 10) {
                    if (c > b) {
                        if (c < a) {
                            return true
                        }
                    }
                }
            }
        }
    }

    return false
}

module.exports = narrowConditionProblem