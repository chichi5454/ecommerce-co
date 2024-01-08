/** @format */

// Function to generate a random card number
function generateCardNumber() {
  // Logic to generate a random card number (you may want to implement a more secure algorithm)
  const cardNumber = Math.floor(Math.random() * 10000000000000000).toString();
  return cardNumber.padStart(16, "0");
}

// Function to generate a card and display it
function generateCard() {
  const fullName = document.getElementById("full_name").value;
  const email = document.getElementById("email").value;
  const contact = document.getElementById("contact").value;
  const userType = document.getElementById("user_type").value;
  const reasonToJoin = document.getElementById("reason_to_join").value;
  const cardNumber = generateCardNumber();

  // Display the generated card details
  document.getElementById(
    "cardOutput"
  ).innerText = `Full Name: ${fullName}\nEmail: ${email}\nContact: ${contact}\nUser Type: ${userType}\nReason to Join: ${reasonToJoin}\nCard Number: ${cardNumber}`;
}

// Function to view a card based on the entered card number
function viewCard() {
  const inputCardNumber = document.getElementById("inputCardNumber").value;

  // Display the entered card number
  document.getElementById(
    "cardOutput"
  ).innerText = `Entered Card Number: ${inputCardNumber}`;
}
