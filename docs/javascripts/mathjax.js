/* Serialize typesetting across Material's instant navigation and startup. */
(() => {
  let pending = Promise.resolve();
  let previousArticle = null;
  const render = () => {
    const engine = window.MathJax;
    if (!engine.startup?.promise || !engine.typesetPromise) return;
    pending = pending.then(() => engine.startup.promise).then(() => {
      const article = document.querySelector('.md-content__inner') || document.body;
      if (previousArticle && previousArticle !== article) {
        engine.typesetClear([previousArticle]);
      }
      previousArticle = article;
      const unrendered = Array.from(article.querySelectorAll('.arithmatex'))
        .filter(element => !element.querySelector('mjx-container'));
      return unrendered.length ? engine.typesetPromise(unrendered) : undefined;
    }).catch(error => console.error('MathJax typesetting failed:', error));
  };
  window.MathJax = {
    tex: {
      inlineMath: [['\\(', '\\)']],
      displayMath: [['\\[', '\\]']],
      processEscapes: true,
      processEnvironments: true,
      tags: 'none'
    },
    options: { ignoreHtmlClass: '.*|', processHtmlClass: 'arithmatex' },
    startup: {
      typeset: false,
      ready() {
        window.MathJax.startup.defaultReady();
        render();
      }
    }
  };
  if (typeof document$ !== 'undefined') document$.subscribe(render);
})();
