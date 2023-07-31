import './Cover.css';

function Cover() {
  return (
    <div className="Cover">
      <header className="Cover-header">
      </header>
      <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
  <header class="mb-auto">
    <div>
      <h3 class="float-md-start mb-0">Cover</h3>
      <nav class="nav nav-masthead justify-content-center float-md-end">
        <a class="nav-link fw-bold py-1 px-0 active" aria-current="page" href="https://getbootstrap.com/">Home</a>
        <a class="nav-link fw-bold py-1 px-0" href="https://getbootstrap.com/">Features</a>
        <a class="nav-link fw-bold py-1 px-0" href="https://getbootstrap.com/">Contact</a>
      </nav>
    </div>
  </header>

  <main class="px-3">
    <h1>BE LOCAL</h1>
    <p class="lead">Be Local is an application that connects Koreans with local knowledge and experience to foreign travelers. Travelers can explore South Korea with locals who are well-acquainted with hidden gems like local eateries and shops, rather than relying on professional guides. This approach presents a new paradigm distinct from conventional travel guide services.</p>
    <p class="lead">
      <a href="https://getbootstrap.com/" class="btn btn-lg btn-light fw-bold border-white bg-white">Learn more</a>
    </p>
  </main>

  <footer class="mt-auto text-white-50">
    <p>Cover template for <a href="https://getbootstrap.com/" class="text-white">Bootstrap</a>, by <a href="https://twitter.com/mdo" class="text-white">@mdo</a>.</p>
  </footer>
</div>
    </div>
  );
}

export default Cover;
