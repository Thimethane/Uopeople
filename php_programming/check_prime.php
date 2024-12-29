<?php
// Program to check if a number is prime

$number = 29; // Example number; you can change this value
$isPrime = true; // Assume the number is prime

// Check divisors from 2 to the square root of the number
if ($number < 2) {
    $isPrime = false; // Numbers less than 2 are not prime
} else {
    for ($i = 2; $i <= sqrt($number); $i++) {
        if ($number % $i == 0) {
            $isPrime = false; // If divisible, the number is not prime
            break;
        }
    }
}

// Display the result
if ($isPrime) {
    echo "$number is a prime number.\n";
} else {
    echo "$number is not a prime number.\n";
}
?>
