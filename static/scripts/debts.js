// Code to show/hide Closed debts block in My debts section

//
//// Code to show/hide Closed debts block in Debts to me section
//const othersDebtsShowButton = document.getElementById("others-debts-show-closed-debts");
//const othersDebtsClosedDebtsBlock = document.getElementById("others-debts-closed-debts-block");
//
//othersDebtsShowButton.addEventListener("click", function(){
//    if (othersDebtsClosedDebtsBlock.style.display === "none" || othersDebtsClosedDebtsBlock.style.display === "") {
//        othersDebtsClosedDebtsBlock.style.display = "block"; // Показать блок
//        othersDebtsShowButton.textContent = "Hide"; // Изменить текст кнопки
//    } else {
//        othersDebtsClosedDebtsBlock.style.display = "none"; // Скрыть блок
//        othersDebtsShowButton.textContent = "Show debts history"; // Изменить текст кнопки
//    }
//});
//
////Code to show/hide Debt form in My Debts section
//const myDebtsAddDebtButton = document.getElementById("my-debts-add-debt-button");
//const addMyDebtForm = document.getElementById("add-my-debt-form");
//
//myDebtsAddDebtButton.addEventListener("click", function(){
//    if (addMyDebtForm.style.display === "none" || addMyDebtForm.style.display === "") {
//        addMyDebtForm.style.display = "";
//    } else {
//        addMyDebtForm.style.display = "none";
//    }
//});
//
////Code to show/hide Debt form in Debts to me section
//const othersDebtsAddDebtButton = document.getElementById("others-debts-add-debt-button");
//const addOthersDebtForm = document.getElementById("add-others-debt-form");
//
//othersDebtsAddDebtButton.addEventListener("click", function(){
//    if (addOthersDebtForm.style.display === "none" || addOthersDebtForm.style.display === "") {
//        addOthersDebtForm.style.display = "block";
//    } else {
//        addOthersDebtForm.style.display = "none";
//    }
//});

document.getElementById('my-debts-add-debt-button').addEventListener('click', function() {
    document.getElementById('add-my-debt-form').style.display = 'block';

    document.getElementById('my-debt-form-action').value = 'create_debt';
    document.getElementById('my-debt-id').value = '';
    document.getElementById('my-debt-form-button').textContent = 'Create debt';

    document.getElementById('my-debt-amount').value = '';
    document.getElementById('my-debt-amount').placeholder = '0';

    document.getElementById('my-debt-creditor-name').value = '';
    document.getElementById('my-debt-date-of-borrowing').value = '';
    document.getElementById('my-debt-repayment-date').value = '';
});

document.getElementById('close-my-debt-form-button').addEventListener('click', function() {
    document.getElementById('add-my-debt-form').style.display = 'none';
});

document.querySelectorAll('.edit-my-debt-button').forEach(button => {
    button.addEventListener('click', function() {
        document.getElementById('add-my-debt-form').style.display = 'block';

        var debtId = this.getAttribute('data-id');
        document.getElementById('my-debt-form-action').value = 'edit_debt';
        document.getElementById('my-debt-id').value = debtId;
        document.getElementById('my-debt-form-button').textContent = 'Save changes';

        var amount = this.getAttribute('data-amount');
        var currency = this.getAttribute('data-currency');
        var creditor = this.getAttribute('data-creditor');
        var dateOfBorrowing = this.getAttribute('data-date-of-borrowing');
        var repaymentDate = this.getAttribute('data-repayment-date');

        document.getElementById('my-debt-amount').value = amount;
        document.getElementById('my-debt-currency').value = currency;
        document.getElementById('my-debt-creditor-name').value = creditor;
        document.getElementById('my-debt-date-of-borrowing').value = dateOfBorrowing;
        document.getElementById('my-debt-repayment-date').value = repaymentDate;
    });
});

document.getElementById('others-debts-add-debt-button').addEventListener('click', function() {
    document.getElementById('add-others-debt-form').style.display = 'block';

    document.getElementById('others-debt-form-action').value = 'create_debt';
    document.getElementById('others-debt-id').value = '';
    document.getElementById('others-debt-form-button').textContent = 'Create debt';

    document.getElementById('others-debt-amount').value = '';
    document.getElementById('others-debt-currency').value = '';
    document.getElementById('id_debtor_name').value = '';
    document.getElementById('others-debt-date-of-borrowing').value = '';
    document.getElementById('others-debt-repayment-date').value = '';
});

document.getElementById('close-others-debt-form-button').addEventListener('click', function() {
    document.getElementById('add-others-debt-form').style.display = 'none';
});

document.querySelectorAll('.edit-others-debt-button').forEach(button => {
    button.addEventListener('click', function() {
        document.getElementById('add-others-debt-form').style.display = 'block';

        var debtId = this.getAttribute('data-id');
        document.getElementById('others-debt-form-action').value = 'edit_debt';
        document.getElementById('others-debt-id').value = debtId;
        document.getElementById('others-debt-form-button').textContent = 'Save changes';

        var amount = this.getAttribute('data-amount');
        var currency = this.getAttribute('data-currency');
        var creditor = this.getAttribute('data-creditor');
        var dateOfBorrowing = this.getAttribute('data-date-of-borrowing');
        var repaymentDate = this.getAttribute('data-repayment-date');

        document.getElementById('others-debt-amount').value = amount;
        document.getElementById('others-debt-currency').value = currency;
        document.getElementById('id_debtor_name').value = creditor;
        document.getElementById('others-debt-date-of-borrowing').value = dateOfBorrowing;
        document.getElementById('others-debt-repayment-date').value = repaymentDate;
    });
});

const myDebtsShowButton = document.getElementById("my-debts-show-closed-debts");
const myDebtsClosedDebtsBlock = document.getElementById("my-debts-closed-debts-block");

myDebtsShowButton.addEventListener("click", function() {
    if (myDebtsClosedDebtsBlock.style.display === "none" || myDebtsClosedDebtsBlock.style.display === "") {
        myDebtsClosedDebtsBlock.style.display = "grid";
        myDebtsShowButton.textContent = "Hide";
    } else {
        myDebtsClosedDebtsBlock.style.display = "none";
        myDebtsShowButton.textContent = "Show debts history";
    }
});

const othersDebtsShowButton = document.getElementById("others-debts-show-closed-debts");
const othersDebtsClosedDebtsBlock = document.getElementById("others-debts-closed-debts-block");

othersDebtsShowButton.addEventListener("click", function() {
    if (othersDebtsClosedDebtsBlock.style.display === "none" || othersDebtsClosedDebtsBlock.style.display === "") {
        othersDebtsClosedDebtsBlock.style.display = "grid";
        othersDebtsShowButton.textContent = "Hide";
    } else {
        othersDebtsClosedDebtsBlock.style.display = "none";
        othersDebtsShowButton.textContent = "Show debts history";
    }
});