import ExecutionEnvironment from '@docusaurus/ExecutionEnvironment';

if (ExecutionEnvironment.canUseDOM) {
  document.addEventListener('click', function(event) {
    if (event.target && event.target.classList.contains('mermaid-enlarge-button')) {
      const button = event.target;
      
      // Find all SVGs that look like Mermaid diagrams
      const allSvgs = Array.from(document.querySelectorAll('svg')).filter(svg => 
        (svg.id && svg.id.startsWith('mermaid-')) || 
        svg.closest('.mermaid') || 
        svg.closest('[class*="mermaid"]')
      );
      
      // Pick the SVG physically preceding the button
      const svg = allSvgs.reverse().find(s => 
        s.compareDocumentPosition(button) & Node.DOCUMENT_POSITION_FOLLOWING
      );
      
      if (svg) {
        const svgClone = svg.cloneNode(true);
        svgClone.setAttribute("xmlns", "http://www.w3.org/2000/svg");
        svgClone.setAttribute("xmlns:xlink", "http://www.w3.org/1999/xlink");
        svgClone.setAttribute("width", "300%");
        svgClone.setAttribute("height", "300%");
        
        const svgData = new XMLSerializer().serializeToString(svgClone);
        const svgBlob = new Blob([svgData], {type: 'image/svg+xml;charset=utf-8'});
        const url = URL.createObjectURL(svgBlob);
        window.open(url, '_blank');
      } else {
        alert("Diagram not found. Please ensure it is fully rendered.");
      }
    }
  });
}