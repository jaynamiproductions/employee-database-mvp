function deleteEquipment(profileid) {
    fetch('/delete-field5', {
    method: 'POST',
    body: JSON.stringify({ profileid: profileid})
    }).then((_res) => {
        window.location.href = "/equipment&it";
    });
}