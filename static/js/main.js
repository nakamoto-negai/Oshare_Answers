// main.js

document.addEventListener('DOMContentLoaded', function() {
  // ----- Slideshow -----
  let slideIndex = 1;
  let slides = document.getElementsByClassName("slide");
  let dots = document.getElementsByClassName("dot");
  let slideshowTimeout; // 自動スライドショーのためのタイマー

  function showSlides(n) {
    if (slides.length === 0 || dots.length === 0) { // スライドやドットがない場合は何もしない
      return;
    }
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}

    for (let i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    for (let i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }

    // slides[slideIndex-1] が存在する場合のみ処理
    if (slides[slideIndex-1]) {
      slides[slideIndex-1].style.display = "block";
    }
    // dots[slideIndex-1] が存在する場合のみ処理
    if (dots[slideIndex-1]) {
      dots[slideIndex-1].className += " active";
    }

    // 自動スライドショーをリセットして再開
    clearTimeout(slideshowTimeout);
    slideshowTimeout = setTimeout(function() { 
      // plusSlides がグローバルに公開されているのでそのまま呼び出す
      if (typeof window.plusSlides === 'function') {
        window.plusSlides(1); 
      }
    }, 5000); // 5秒ごとに画像を切り替え
  }

  // plusSlides と currentSlide をグローバルスコープに公開 (HTMLのonclickから呼び出せるように)
  window.plusSlides = function(n) {
    showSlides(slideIndex += n);
  }

  window.currentSlide = function(n) {
    showSlides(slideIndex = n);
  }

  // 初期表示と自動スライドショー開始
  if (slides.length > 0) { // スライドが存在する場合のみ実行
      showSlides(slideIndex);
  }
  // ----- End Slideshow -----


  // ----- Category Image Grid -----
  const imageGridContainer = document.getElementById('image-grid-container');
  const categoryButtons = document.querySelectorAll('.category-buttons button');

  // 表示する画像のサンプルデータです。
  // 実際の画像のパスとカテゴリーに合わせてください。
  // home_preview.html と同じ階層に 'images' フォルダを作り、
  // その中に 'men_1.jpg', 'women_1.jpg' などの画像を配置することを想定しています。
  const imageData = [
    // MEN カテゴリ (12枚例)
    { src: '/static/images/men_1.jpg', category: 'men', alt: '男性ファッション 1' },
    { src: '/static/images/men_2.jpg', category: 'men', alt: '男性ファッション 2' },
    { src: '/static/images/men_3.jpg', category: 'men', alt: '男性ファッション 3' },
    { src: '/static/images/men_4.jpg', category: 'men', alt: '男性ファッション 4' },
    { src: '/static/images/men_5.jpg', category: 'men', alt: '男性ファッション 5' },
    { src: '/static/images/men_6.jpg', category: 'men', alt: '男性ファッション 6' },
    { src: '/static/images/men_7.jpg', category: 'men', alt: '男性ファッション 7' },
    { src: '/static/images/men_8.jpg', category: 'men', alt: '男性ファッション 8' },
    

    // WOMEN カテゴリ (12枚例)
    { src: '/static/images/women_1.jpg', category: 'women', alt: '女性ファッション 1' },
    { src: '/static/images/women_2.jpg', category: 'women', alt: '女性ファッション 2' },
    { src: '/static/images/women_3.jpg', category: 'women', alt: '女性ファッション 3' },
    { src: '/static/images/women_4.jpg', category: 'women', alt: '女性ファッション 4' },
    { src: '/static/images/women_5.jpg', category: 'women', alt: '女性ファッション 5' },
    { src: '/static/images/women_6.jpg', category: 'women', alt: '女性ファッション 6' },
    { src: '/static/images/women_7.jpg', category: 'women', alt: '女性ファッション 7' },
    { src: '/static/images/women_8.jpg', category: 'women', alt: '女性ファッション 8' },
    
    // KIDS カテゴリ (12枚例)
    { src: '/static/images/kids_1.jpg', category: 'kids', alt: '子供服ファッション 1' },
    { src: '/static/images/kids_2.jpg', category: 'kids', alt: '子供服ファッション 2' },
    { src: '/static/images/kids_3.jpg', category: 'kids', alt: '子供服ファッション 3' },
    { src: '/static/images/kids_4.jpg', category: 'kids', alt: '子供服ファッション 4' },
    { src: '/static/images/kids_5.jpg', category: 'kids', alt: '子供服ファッション 5' },
    { src: '/static/images/kids_6.jpg', category: 'kids', alt: '子供服ファッション 6' },
    { src: '/static/images/kids_7.jpg', category: 'kids', alt: '子供服ファッション 7' },
    { src: '/static/images/kids_8.jpg', category: 'kids', alt: '子供服ファッション 8' }
    // 他の画像も同様に追加 (必要に応じて)
  ];

  function displayImages(selectedCategory) {
    // imageGridContainer が null (存在しない) 場合、処理を中断
    if (!imageGridContainer) {
      // console.error('Error: Image grid container not found!'); // デバッグ用
      return;
    }
    imageGridContainer.innerHTML = ''; // グリッド内の既存の画像をクリア

    const filteredImages = selectedCategory === 'all'
      ? imageData // 'all' の場合は全ての画像
      : imageData.filter(image => image.category === selectedCategory);

    // 4x3 グリッドなので、最大12枚表示 (sliceで枚数制限)
    const imagesToDisplay = filteredImages.slice(0, 12);

    imagesToDisplay.forEach(imageInfo => {
      const imgElement = document.createElement('img');
      imgElement.src = imageInfo.src;
      imgElement.alt = imageInfo.alt || selectedCategory + ' image'; // alt属性を設定
      imageGridContainer.appendChild(imgElement);
    });
  }

  if (categoryButtons.length > 0) { // カテゴリーボタンが存在する場合のみイベントリスナーを設定
    categoryButtons.forEach(button => {
      button.addEventListener('click', function() {
        const selectedCategory = this.dataset.category; // クリックされたボタンのdata-categoryの値を取得

        // (任意)選択されたボタンに 'active-category' クラスを付け、他からは削除
        categoryButtons.forEach(btn => btn.classList.remove('active-category'));
        this.classList.add('active-category');

        displayImages(selectedCategory);
      });
    });
  }


  // (任意)ページ読み込み時にデフォルトで表示するカテゴリ（例: 'all' または最初のカテゴリ）
  if (categoryButtons.length > 0 && imageGridContainer) {
    let defaultCategoryToShow = 'all';
    let activeButton = document.querySelector('.category-buttons button[data-category="all"]');
    
    if (activeButton) { // "ALL" ボタンがあればそれをアクティブに
      activeButton.classList.add('active-category');
    } else if (categoryButtons.length > 0) { // "ALL"ボタンがない場合、最初のボタンをアクティブにする
      categoryButtons[0].classList.add('active-category');
      defaultCategoryToShow = categoryButtons[0].dataset.category;
    }
    displayImages(defaultCategoryToShow);
  }
  // ----- End Category Image Grid -----


  // 他のJavaScriptコード (例: フォーム送信時の確認など)
  // このコードは home.html に <form> タグがないと機能しません。
  // home.html の検索フォームはコメントアウトされているため、現状ではこの部分は実行されても対象がありません。
  const allForms = document.querySelectorAll('form');
  if (allForms.length > 0) {
    allForms.forEach(function(form) {
      form.addEventListener('submit', function(event) {
        // event.preventDefault(); // 必要なら送信を止める
        console.log('フォームが送信されようとしています。');
      });
    });
  }

});

