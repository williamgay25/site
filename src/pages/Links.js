import React from 'react';
import Nav from '../components/Nav';

function Blog() {
  return (
    <div>
      <header>
        <h1>links</h1>
        <Nav />
      </header>

      <section>
        <ul>
          <li><a href="https://www.lesswrong.com/posts/wEebEiPpEwjYvnyqq/when-money-is-abundant-knowledge-is-the-real-wealth">When Money is Abundant, Knowledge is the Real Wealth</a></li>
        </ul> 
      </section>
    </div>
  );
}

export default Blog;