import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Blog from './pages/Blog';
import Books from './pages/Books';
import Links from './pages/Links';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/blog" element={<Blog />} />
        <Route path="/books" element={<Books />} />
        <Route path="/links" element={<Links />} />
      </Routes>
    </Router>
  );
}

export default App;

