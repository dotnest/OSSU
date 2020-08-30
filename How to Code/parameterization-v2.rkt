;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname parameterization-v2) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;(define (contains-ubc? los) false) ;stub

(define (contains-ubc? los) (contains? "UBC" los))

;(define (contains-mcgill? los) false) ;stub

(define (contains-mcgill? los) (contains? "McGill" los))

(check-expect (contains? "UBC" empty) false)
(check-expect (contains? "UBC" (cons "UBC" empty)) true)
(check-expect (contains? "UBC" (cons "McGill" empty)) false)
(check-expect (contains? "UBC" (cons "UBC" (cons "McGill" empty))) true)
(check-expect (contains? "UBC" (cons "McGill" (cons "UBC" empty))) true)
(check-expect (contains? "Toronto" (cons "McGill" (cons "UBC" empty))) false)

;; ListOfString -> Boolean
;; produce true if los includes s
(define (contains? s los)
  (cond [(empty? los) false]
        [else
         (if (string=? (first los) s)
             true
             (contains? s (rest los)))]))


;; ====================

;(define (squares lon) empty) ;stub

(define (squares lon) (map2 sqr lon))

;(define (square-roots lon) empty) ;stub

(define (square-roots lon) (map2 sqrt lon))

(check-expect (map2 sqr empty) empty)
(check-expect (map2 sqr (list 3 4)) (list 9 16))
(check-expect (map2 sqrt (list 9 16)) (list 3 4))
(check-expect (map2 abs (list 9 -7 16)) (list 9 7 16))

;; ListOfNumber -> ListOfNumber
;; given fn and (list n0 n1 ...), return (list (fn n0) (fn n1) ...)
(define (map2 fn lon)
  (cond [(empty? lon) empty]
        [else
         (cons (fn (first lon))
               (map2 fn (rest lon)))]))


;; ====================

;(define (positive-only lon) empty) ;stub

(define (positive-only lon) (filter2 positive? lon))

;(define (negative-only lon) empty) ;stub

(define (negative-only lon) (filter2 negative? lon))

(check-expect (filter2 positive? empty) empty)
(check-expect (filter2 positive? (list 1 -2 3 -4)) (list 1 3))
(check-expect (filter2 negative? (list 1 -2 3 -4)) (list -2 -4))

;; ListOfNumber -> ListOfNumber
;; produce list with only those elements of lon which produce true for (pred n)
(define (filter2 pred lon)
  (cond [(empty? lon) empty]
        [else
         (if (pred (first lon))
             (cons (first lon)
                   (filter2 pred (rest lon)))
             (filter2 pred (rest lon)))]))
