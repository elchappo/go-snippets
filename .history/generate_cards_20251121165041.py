#!/usr/bin/env python3
import json

algorithms = [
    {"cat": "array", "title": "Remove Duplicates", "desc": "Two-pointer technique for sorted arrays", "time": "O(n)", "space": "O(1)", "pros": ["In-place", "Single pass"], "cons": ["Sorted only"], "usage": "Remove duplicates without extra space"},
    {"cat": "stack", "title": "Valid Parentheses", "desc": "Stack-based bracket validation", "time": "O(n)", "space": "O(n)", "pros": ["Multiple types", "Single pass"], "cons": ["Extra space"], "usage": "Validate balanced expressions"},
    {"cat": "linked", "title": "Reverse Linked List", "desc": "Recursive list reversal", "time": "O(n)", "space": "O(n)", "pros": ["Clean solution"], "cons": ["Stack space"], "usage": "List reversal"},
    {"cat": "sorting", "title": "Insertion Sort", "desc": "Build sorted array incrementally", "time": "O(n²)", "space": "O(1)", "pros": ["Simple", "Stable"], "cons": ["Slow for large data"], "usage": "Small datasets"},
    {"cat": "sorting", "title": "Merge Sort", "desc": "Divide and conquer sorting", "time": "O(n log n)", "space": "O(n)", "pros": ["Guaranteed O(n log n)", "Stable"], "cons": ["Extra space"], "usage": "Stable sort needed"},
    {"cat": "sorting", "title": "Quick Sort", "desc": "Pivot-based partitioning", "time": "O(n log n)", "space": "O(log n)", "pros": ["Fast average", "In-place"], "cons": ["Unstable", "O(n²) worst"], "usage": "General purpose"},
    {"cat": "search", "title": "Binary Search", "desc": "Divide search interval in half", "time": "O(log n)", "space": "O(1)", "pros": ["Very fast", "Simple"], "cons": ["Sorted array needed"], "usage": "Search sorted arrays"},
    {"cat": "tree", "title": "Binary Search Tree", "desc": "Ordered tree structure", "time": "O(log n)", "space": "O(log n)", "pros": ["Fast search", "Ordered"], "cons": ["Can be unbalanced"], "usage": "Ordered data storage"},
    {"cat": "tree", "title": "BFS Level Order", "desc": "Breadth-first tree traversal", "time": "O(n)", "space": "O(n)", "pros": ["Level by level"], "cons": ["Queue space"], "usage": "Level-wise processing"}
]

html = """<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Go Algorithms</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);min-height:100vh;padding:20px}.container{max-width:1400px;margin:0 auto}header{text-align:center;color:white;margin-bottom:40px;padding:30px;background:rgba(255,255,255,0.1);border-radius:15px}header h1{font-size:2.5em;margin-bottom:10px}header p{font-size:1.2em}.section-nav{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:30px}.section-btn{padding:10px 20px;background:white;border:none;border-radius:25px;cursor:pointer;font-weight:600;transition:all 0.3s}.section-btn:hover{transform:translateY(-2px)}.section-btn.active{background:#667eea;color:white}.cards-container{display:grid;grid-template-columns:repeat(auto-fill,minmax(400px,1fr));gap:25px}.card{background:white;border-radius:15px;padding:25px;box-shadow:0 10px 30px rgba(0,0,0,0.2);transition:all 0.3s}.card:hover{transform:translateY(-5px)}.card-title{font-size:1.5em;font-weight:700;margin-bottom:15px;color:#667eea;border-bottom:3px solid #667eea;padding-bottom:10px}.card-description{font-size:0.95em;color:#666;margin-bottom:15px}.complexity{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:15px}.complexity-item{background:#f8f9fa;padding:10px;border-radius:8px;border-left:4px solid #667eea}.complexity-label{font-size:0.8em;color:#666;font-weight:600}.complexity-value{font-size:1.1em;font-weight:700;font-family:monospace}.pros-cons{display:grid;grid-template-columns:1fr 1fr;gap:15px;margin-bottom:15px}.pros,.cons{background:#f8f9fa;padding:15px;border-radius:8px}.pros{border-left:4px solid #28a745}.cons{border-left:4px solid #dc3545}.pros h4{color:#28a745;margin-bottom:10px;font-size:0.9em}.cons h4{color:#dc3545;margin-bottom:10px;font-size:0.9em}.pros ul,.cons ul{list-style:none;padding-left:0}.pros li:before{content:"✓ ";color:#28a745;font-weight:bold}.cons li:before{content:"✗ ";color:#dc3545;font-weight:bold}.usage{background:#fff3cd;border-left:4px solid #ffc107;padding:12px;border-radius:8px;margin-bottom:15px}.usage-label{font-weight:700;color:#856404;font-size:0.85em}.usage-text{color:#856404;font-size:0.9em}@media (max-width:768px){.cards-container{grid-template-columns:1fr}.pros-cons,.complexity{grid-template-columns:1fr}}</style>
</head><body><div class="container"><header><h1>🚀 Go Algorithms & Data Structures</h1><p>Interactive Memory Cards</p></header>
<div class="section-nav"><button class="section-btn active" onclick="filter('all')">All</button><button class="section-btn" onclick="filter('array')">Arrays</button><button class="section-btn" onclick="filter('stack')">Stack</button><button class="section-btn" onclick="filter('linked')">Linked Lists</button><button class="section-btn" onclick="filter('sorting')">Sorting</button><button class="section-btn" onclick="filter('search')">Search</button><button class="section-btn" onclick="filter('tree')">Trees</button></div>
<div id="cards" class="cards-container"></div></div>
<script>
const algos=""" + json.dumps(algorithms) + """;
let cur='all';
function filter(cat){cur=cat;document.querySelectorAll('.section-btn').forEach(b=>b.classList.remove('active'));event.target.classList.add('active');render();}
function render(){const c=document.getElementById('cards');c.innerHTML='';algos.forEach((a,i)=>{if(cur!='all'&&a.cat!=cur)return;c.innerHTML+=`<div class="card"><div class="card-title">${a.title}</div><div class="card-description">${a.desc}</div><div class="complexity"><div class="complexity-item"><div class="complexity-label">Time</div><div class="complexity-value">${a.time}</div></div><div class="complexity-item"><div class="complexity-label">Space</div><div class="complexity-value">${a.space}</div></div></div><div class="pros-cons"><div class="pros"><h4>Pros</h4><ul>${a.pros.map(p=>'<li>'+p+'</li>').join('')}</ul></div><div class="cons"><h4>Cons</h4><ul>${a.cons.map(p=>'<li>'+p+'</li>').join('')}</ul></div></div><div class="usage"><div class="usage-label">Usage</div><div class="usage-text">${a.usage}</div></div></div>`;});}
render();
</script></body></html>"""

with open('index.html', 'w') as f:
    f.write(html)

print("Generated index.html successfully!")
