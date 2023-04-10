function deletePayroll(profileid) {
    fetch('/delete-field10', {
    method: 'POST',
    body: JSON.stringify({ profileid: profileid})
    }).then((_res) => {
        window.location.href = "/payroll";
    });
}