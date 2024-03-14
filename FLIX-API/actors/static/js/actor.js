async function getActors(){ 
    try {
        const response = await fetch("/actors/1", {
          method: "GET",
          
        });
    
        const data = await response.json();
    
        if (response.ok) {
            document.getElementById('id').textContent=data.id;
            document.getElementById('name').textContent=data.name;
            document.getElementById('birthday').textContent=data.birthday;
            document.getElementById('nationality').textContent=data.nationality;
        } else {
          
        }
      } catch (error) {
        console.error("Oops, an error occurred");
      }

 }
 
 getActors()