
# XML Exercises Project

This project is a collection of exercises to help understand and practice XML syntax, structure, and applications. Each exercise focuses on different aspects of XML, including document creation, data representation, and tree structure visualization.

## Exercises Overview

### Exercise 1: Describe the Exercises
Create an XML document to describe the exercises in this document.

- **Specifications**:
  - The root element is `<exercises>` with an attribute `number` set to `1`.
  - The root contains three child elements:
    - `<date>`: Specifies the date of the exercise.
    - Two `<item>` elements for the first two exercises.
  - Add descriptive text inside the `<item>` elements.

- **Example XML**:
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <exercises number="1">
      <date>2024-12-24</date>
      <item>Write an XML document to describe these exercises.</item>
      <item>Write an XML document to describe a person with suitable nesting.</item>
  </exercises>
  ```

### Exercise 2: Describe a Person
Create an XML document to describe a person using fake data.

- **Specifications**:
  - Include the following details:
    - Name
    - Occupation
    - Address
    - Hobbies
  - Use suitable element names and nesting.
  - Ensure the document is well-formed.

- **Example XML**:
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <person>
      <name>Jane Doe</name>
      <occupation>Software Developer</occupation>
      <address>
          <street>123 Main Street</street>
          <city>Springfield</city>
          <state>IL</state>
          <zipcode>62704</zipcode>
      </address>
      <hobbies>
          <hobby>Reading</hobby>
          <hobby>Hiking</hobby>
          <hobby>Photography</hobby>
      </hobbies>
  </person>
  ```

### Exercise 3: Draw an XML Tree
Visualize the XML document created in Exercise 2 by drawing its tree representation.

- **Specifications**:
  - Represent the structure and nesting of the XML elements as a hierarchical tree.
  - Include all elements, attributes (if any), and nesting levels.

### Exercise 4: Create a Program of Study XML
Create an XML document, `programOfStudy.xml`, to represent a student's program of study.

- **Specifications**:
  - Include semesters (`Fall 2008` and `Spring 2009`) as parent elements.
  - Each semester contains child elements for courses:
    - General Education courses with goals.
    - Core courses.
    - Major courses.
  - Include course details like name and goal (for General Education).

- **Example XML**:
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <programOfStudy>
      <semester name="Fall 2008">
          <generalEducation>
              <course code="PHIL 101" goal="8">Introduction to Philosophy</course>
              <course code="ECON 201" goal="11">Principles of Economics</course>
          </generalEducation>
          <coreCourses>
              <course code="MGT 217">Management Principles</course>
          </coreCourses>
          <majorCourses>
              <course code="CIS 120">Introduction to Information Systems</course>
              <course code="CIS 403">Database Management</course>
          </majorCourses>
      </semester>
      <semester name="Spring 2009">
          <coreCourses>
              <course code="MGT 261">Organizational Behavior</course>
              <course code="MKTG 325">Marketing Principles</course>
          </coreCourses>
          <majorCourses>
              <course code="CIS 220">Advanced Programming</course>
              <course code="CIS 407">System Analysis and Design</course>
              <course code="CIS 490">Capstone Project</course>
          </majorCourses>
      </semester>
  </programOfStudy>
  ```

## How to Use This Repository

1. **Exercise 1**: Create a file named `exercise1.xml` and write the XML document as per the instructions.
2. **Exercise 2**: Create a file named `exercise2.xml` with the XML document describing a person.
3. **Exercise 3**: Represent the XML from Exercise 2 as a tree diagram. This can be done using drawing software or even on paper.
4. **Exercise 4**: Create a file named `programOfStudy.xml` with the XML document for the program of study.

## Validation and Testing

- Ensure all XML files are well-formed by using an XML validator or an IDE that supports XML (e.g., VS Code, Eclipse).
- Use tools like **TreeViewer** or online XML tree generators to visualize the hierarchy in Exercise 3.

---

This project serves as an introduction to XML syntax, data structuring, and visualization. Complete each exercise and validate your files to gain a strong foundational understanding of XML.
