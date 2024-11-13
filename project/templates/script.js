// script.js

// Function to handle adding a new expense
function addExpense(event) {
    event.preventDefault(); // Prevent the form from submitting

    // Get values from the form inputs
    const expenseName = document.getElementById('expense-name').value;
    const expenseAmount = document.getElementById('expense-amount').value;
    const expenseDate = document.getElementById('expense-date').value;
    const expenseCategory = document.getElementById('expense-category').value;

    // Create a new table row for the expense
    const newRow = document.createElement('tr');

    newRow.innerHTML = `
        <td class="py-2 px-4 border-b">${expenseName}</td>
        <td class="py-2 px-4 border-b">$${parseFloat(expenseAmount).toFixed(2)}</td>
        <td class="py-2 px-4 border-b">${expenseDate}</td>
        <td class="py-2 px-4 border-b">${expenseCategory}</td>
        <td class="py-2 px-4 border-b">
            <button class="text-blue-600 hover:underline" onclick="editExpense(this)">Edit</button>
            <button class="text-red-600 hover:underline" onclick="deleteExpense(this)">Delete</button>
        </td>
    `;

    // Append the new row to the expense list table
    const expenseTableBody = document.querySelector('tbody');
    expenseTableBody.appendChild(newRow);

    // Clear the form inputs
    document.getElementById('expense-name').value = '';
    document.getElementById('expense-amount').value = '';
    document.getElementById('expense-date').value = '';
    document.getElementById('expense-category').value = 'Food'; // Reset to default
}

// Function to handle editing an expense
function editExpense(button) {
    const row = button.closest('tr');
    const cells = row.querySelectorAll('td');

    // Populate the form with the current values
    document.getElementById('expense-name').value = cells[0].innerText;
    document.getElementById('expense-amount').value = parseFloat(cells[1].innerText.replace('$', '')).toFixed(2);
    document.getElementById('expense-date').value = cells[2].innerText;
    document.getElementById('expense-category').value = cells[3].innerText;

    // Remove the row from the table
    row.remove();
}

// Function to handle deleting an expense
function deleteExpense(button) {
    const row = button.closest('tr');
    row.remove();
}

// Attach the addExpense function to the form submission
document.querySelector('form').addEventListener('submit', addExpense);