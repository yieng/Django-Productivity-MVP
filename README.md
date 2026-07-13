# Goal-Oriented Productivity Dashboard (Django MVP)

A custom, high-velocity task management system built to solve a specific problem: bridging the gap between daily execution and long-term financial goals. Unlike generic productivity apps, this system uses a weighted, goal-aligned credit logic to prioritize high-value work.

## Technical Architecture
This project utilizes the Django MVT (Model-View-Template) architectural pattern.

* **Custom Business Logic:** Implemented dynamic credit calculation via Django model `@property` methods. This allows for weighted task prioritization (e.g., "Finance" tasks are valued higher than "Flex" tasks), which directly impacts financial progress tracking.
* **Database Management:** Utilized Django's ORM to abstract SQLite database operations, ensuring data integrity and simplified schema management.
* **Responsive UI:** Integrated Bootstrap 5 to ensure a clean, modern, and mobile-friendly interface, critical for quick task entry while on the move.
* **Deployment Lifecycle:** Managed the full deployment pipeline, including schema evolution through Django migrations (`makemigrations`, `migrate`) and automated environment initialization.

## Engineering Narrative: Why Django?
I chose Django for this project because of its "batteries-included" philosophy. Managing CSRF protection, secure form handling, and user-state persistence natively allowed me to focus on the business logic—my specific credit-weighting algorithm—rather than reinventing infrastructure.

## Developer's Log
"During the development of this MVP, the primary challenge was implementing dynamic, goal-weighted credit accumulation. Instead of storing a static 'points' value in the database (which creates data-integrity risks), I implemented a computed property within the Django Model. This ensures that the 'Fund Balance' is always an accurate, real-time reflection of completed tasks, significantly increasing the reliability of the dashboard as a source of truth for my financial goal-setting."

---
*Created as a high-velocity MVP to track progress toward a $200k AUD gross income objective.*