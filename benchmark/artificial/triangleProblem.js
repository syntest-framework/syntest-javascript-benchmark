
function triangleProblem(a, b, c) {
    if (typeof a !== 'number') {
        return 'invalid'
    }

    if (typeof b !== 'number') {
        return 'invalid'
    }

    if (typeof c !== 'number') {
        return 'invalid'
    }

    // if (a + b <= c) {
    //     return 'invalid'
    // }

    // if (a + c <= b) {
    //     return 'invalid'
    // }

    // if (a + c <= b) {
    //     return 'invalid'
    // }
    
    if (a === b) {
        if (b === c) {
            return "E"
        } else {
            return "I"
        }
    } else if (b === c) {
        return "I"
    } else {
        return "S"
    }
}

module.exports = triangleProblem
