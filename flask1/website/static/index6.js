function deleteEmp_health(profileid) {
    fetch('/delete-field6', {
    method: 'POST',
    body: JSON.stringify({ profileid: profileid})
    }).then((_res) => {
        window.location.href = "/employee-health";
    });
}