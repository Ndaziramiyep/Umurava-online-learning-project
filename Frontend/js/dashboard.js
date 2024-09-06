// script.js
document.addEventListener('DOMContentLoaded', () => {
    const content = document.getElementById('content');
    
    const loadContent = (section) => {
        switch(section) {
            case 'overview':
                content.innerHTML = `<h2>Overview</h2><p>Here is a brief overview of your eCommerce dashboard.</p>`;
                break;
            case 'sales':
                content.innerHTML = `<h2>Sales</h2><p>Sales data and analytics will be displayed here.</p>`;
                break;
            case 'products':
                content.innerHTML = `<h2>Products</h2><p>Manage and view your products here.</p>`;
                break;
            case 'customers':
                content.innerHTML = `<h2>Customers</h2><p>Customer information and statistics will be shown here.</p>`;
                break;
            case 'reports':
                content.innerHTML = `<h2>Reports</h2><p>Generate and view various reports here.</p>`;
                break;
            default:
                content.innerHTML = `<h2>Welcome</h2><p>Select a section from the sidebar to get started.</p>`;
                break;
        }
    };

    document.querySelectorAll('.sidebar a').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const section = e.target.id;
            loadContent(section);
        });
    });

    // Load default content
    loadContent('overview');
});
