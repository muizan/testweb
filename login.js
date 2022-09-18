import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.3/firebase-app.js";
import { getDatabase,ref,set,push} from "https://www.gstatic.com/firebasejs/9.9.3/firebase-database.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDCCYa6k7F25nnej5XWZ_EKH6tFPucfQNI",
  authDomain: "my-web-scrapper-3dff1.firebaseapp.com",
  databaseURL: "https://my-web-scrapper-3dff1-default-rtdb.firebaseio.com",
  projectId: "my-web-scrapper-3dff1",
  storageBucket: "my-web-scrapper-3dff1.appspot.com",
  messagingSenderId: "821149662981",
  appId: "1:821149662981:web:f2a947cfd6adab9550016c"
};
// alert('sunmot');
// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getDatabase();
document.getElementById('data').addEventListener('submit',register);

function register(e){
    e.preventDefault();
    const productlink = document.getElementById('prod').value  
    const price = document.getElementById('num').value 
    const email = document.getElementById('nm').value 
    // console.log('e', e)
    // console.log(productlink, price, email)

    saveMessage(productlink,price,email);
}
function saveMessage(productlink,price,email){
   // console.log('WOrking')
    const messagesRef = getDatabase();
    console.log(messagesRef)
    push(ref(messagesRef,'customerList/'),{
        productlink:productlink,
        price:price,
        email:email
    });
    alert('your project has been registered')
   // window.location.replace('/templates/notified.html')
    
}
