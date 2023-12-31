(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond 
    ((< x 0) -1)
    ((= x 0) 0)
    (else 1))
)

(define (square x) (* x x))

(define (pow b n)
  (cond
    ((= n 1) b)
    ((= (modulo n 2) 0) (pow (square b) (/ n 2)))
    (else (* b (pow b (- n 1)))))
)

(define (ordered? s)
  (cond 
    ((null? (cdr s)) #t)
    ((> (car s) (cadr s)) #f) 
    (else (ordered? (cdr s))))
)

(define (nodots s)
  (cond 
    ((integer? s) (list s))
    ((and (list? s) (=(length s) 1)) s)
    ((integer? (car s)) (append (list (car s)) (nodots (cdr s))))
    (else (append (list (nodots (car s))) (nodots (cdr s))))) 
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ((> (car s) v) false)
          ((= (car s) v) true)
          (else (contains? (cdr s) v)))
  )

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((< v (car s)) (append (list v) s))
          ((= (car s) v) s)
          (else (append (list (car s)) (add (cdr s) v))))
          )

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (append (list (car s)) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          ((< (car t) (car s)) (intersect s (cdr t))))
          )

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (append (list (car s)) (union (cdr s) (cdr t))))
          ((< (car s) (car t)) (append (list (car s)) (union (cdr s) t)))
          ((< (car t) (car s)) (append (list (car t)) (union s (cdr t)))))
          )

; Q9 - Survey
(define (survey)
    ; Midsemester Survey: https://goo.gl/forms/DJozOAVLzfXARJGn2
    'parenthesis
)