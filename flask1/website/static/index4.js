function deleteEmp_notes(profileid) {
    fetch('/delete-field4', {
    method: 'POST',
    body: JSON.stringify({ profileid: profileid})
    }).then((_res) => {
        window.location.href = "/employee-notes";
    });
}