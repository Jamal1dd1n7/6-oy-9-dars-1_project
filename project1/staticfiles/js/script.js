let body = document.querySelector("body");
let button = document.querySelector("#switch"); // Tugmani tanlash
let isToggled = false;

button.onclick = () => {
    isToggled = !isToggled; // Holatni o'zgartirish
    body.style.setProperty("--value", isToggled ? "black" : "white");
};

  // Xabarlarni JavaScript-ga o'tkazish
  

  // Xabarlarni konsolga chiqarish
  console.log(messages);

  // Dinamik xabarlarni DOM ga qo'shish
  const container = document.createElement('div');
  container.style.position = 'fixed';
  container.style.top = '10px';
  container.style.left = '50%';
  container.style.transform = 'translateX(-50%)';
  container.style.zIndex = '1050';

  messages.forEach(message => {
      const alertDiv = document.createElement('div');
      alertDiv.className = `alert alert-${message.tag === "error" ? "danger" : message.tag} alert-dismissible fade show`;
      alertDiv.innerHTML = `
          ${message.text}
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      `;
      container.appendChild(alertDiv);
  });

  document.body.appendChild(container);

  // Avtomatik tarzda xabarlarni 5 soniyadan keyin o'chirish
  setTimeout(() => {
      container.remove();
  }, 5000);