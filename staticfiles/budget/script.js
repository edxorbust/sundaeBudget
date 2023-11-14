


document.addEventListener("DOMContentLoaded", function() {
    const recurrentCheckbox = document.querySelector('#recurrent');
    const frecuencySelect = document.querySelector('#frecuencySelect');
    const currentLocation = location.href;
    const menuItem = document.querySelectorAll('.itt');
    const menuLength = menuItem.length;
    for (let i=0; i< menuLength; i++){
        if(menuItem[i].href === currentLocation){
            menuItem[i].classList.add('active')
        }
    }


    if (frecuencySelect !== null){
        frecuencySelect.disabled = !this.checked;
    }
    
    if (recurrentCheckbox !== null){
        recurrentCheckbox.addEventListener('change', function () {
            frecuencySelect.disabled = !this.checked;
        });
    }

    if (document.getElementById('remaining-budget') !== null){

        const remainigBudget = document.getElementById('remaining-budget').innerHTML;
        const myModal = new bootstrap.Modal('#exampleModalCenter');
        const myModal2 = new bootstrap.Modal('#exampleModalCenter2');
        if (parseFloat(remainigBudget) < 0) {
            document.getElementById('remaining-div').style.backgroundColor = '#ef5459';
            document.getElementById('remaining-text').style.color = 'white';
            document.getElementById('rem-sep').style.backgroundColor = 'white';
            myModal.show();

        }

        if (parseFloat(remainigBudget) < 50 && parseFloat(remainigBudget) > 0) {
            document.getElementById('remaining-div').style.backgroundColor = '#ffe100';
            document.getElementById('remaining-text').style.color = 'black';
            document.getElementById('rem-sep').style.backgroundColor = 'white';
            myModal2.show();

        }

        document.getElementById('closeButton').addEventListener('click', () => {
            myModal.hide();
        })
        document.getElementById('closeButton2').addEventListener('click', () => {
            myModal2.hide();
        })
    }

   

    
    
});



