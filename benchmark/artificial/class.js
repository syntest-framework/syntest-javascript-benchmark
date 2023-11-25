class X {
    _current
    
    constructor //*(*(8))
    (y) {
        this.x = y
    }
    

    change(mutation) {
        this._current += mutation
    }

    set current(value) {
        this._current = value
    }

    get current() {
        return this._current
    }
}

class Z {
    _current

    set current(value) {
        this._current = value
    }

    get current() {
        return this._current
    }
}

function createX() {
    return new X()
}

function Y () {
    console.log()
}

Y.prototype = {
    a: () => {
        console.log('Y.a')
    },
    b () {}
}
Y.prototype.c = function () {}

const A = {
    a: () => {
        console.log('A.a')
    }
}
A.b = () => {
    console.log('A.b')
}
A.prototype = {
    c: () => {
        console.log('A.c')
    }
}

function B () {
    this.a = 5
}


exports.X = X
// exports.Y = Y
// exports.Z = Z

// exports.A = A
// exports.B = B

// exports.createX = createX
