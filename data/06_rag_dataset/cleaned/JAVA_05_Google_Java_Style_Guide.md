<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Begin Jekyll SEO tag v2.8.0 -->
<title>Google Java Style Guide | Google Style Guides</title>
<meta name="generator" content="Jekyll v3.10.0" />
<meta property="og:title" content="Google Java Style Guide" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="Style guides for Google-originated open-source projects" />
<meta property="og:description" content="Style guides for Google-originated open-source projects" />
<link rel="canonical" href="https://google.github.io/styleguide/javaguide.html" />
<meta property="og:url" content="https://google.github.io/styleguide/javaguide.html" />
<meta property="og:site_name" content="Google Style Guides" />
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary" />
<meta property="twitter:title" content="Google Java Style Guide" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"WebPage","description":"Style guides for Google-originated open-source projects","headline":"Google Java Style Guide","url":"https://google.github.io/styleguide/javaguide.html"}</script>
<!-- End Jekyll SEO tag -->

    <link rel="stylesheet" href="/styleguide/assets/css/style.css?v=7c3eb00dd3a3308003c5c8a79c4290dc1c8a8c53">
    <link rel="shortcut icon" type="image/x-icon" href="/styleguide/favicon.ico">
<link rel="stylesheet" href="/styleguide/include/mdguide.css">
<script type="module" src="/styleguide/include/mdguide_main.js"></script>

  </head>
  <body>
    <div class="container-lg px-3 my-5 markdown-body">

      <h1><a href="https://google.github.io/styleguide/">Google Style Guides</a></h1>


      <h1 id="google-java-style-guide">Google Java Style Guide</h1>

<!-- mdformat off -->
<ul id="markdown-toc">
  <li><a href="#google-java-style-guide" id="markdown-toc-google-java-style-guide">Google Java Style Guide</a>    <ul>
      <li><a href="#1-introduction" id="markdown-toc-1-introduction">1 Introduction</a>        <ul>
          <li><a href="#11-terminology-notes" id="markdown-toc-11-terminology-notes">1.1 Terminology notes</a></li>
          <li><a href="#12-guide-notes" id="markdown-toc-12-guide-notes">1.2 Guide notes</a></li>
        </ul>
      </li>
      <li><a href="#2-source-file-basics" id="markdown-toc-2-source-file-basics">2 Source file basics</a>        <ul>
          <li><a href="#21-file-name" id="markdown-toc-21-file-name">2.1 File name</a></li>
          <li><a href="#22-file-encoding-utf-8" id="markdown-toc-22-file-encoding-utf-8">2.2 File encoding: UTF-8</a></li>
          <li><a href="#23-special-characters" id="markdown-toc-23-special-characters">2.3 Special characters</a>            <ul>
              <li><a href="#231-whitespace-characters" id="markdown-toc-231-whitespace-characters">2.3.1 Whitespace characters</a></li>
              <li><a href="#232-special-escape-sequences" id="markdown-toc-232-special-escape-sequences">2.3.2 Special escape sequences</a></li>
              <li><a href="#233-non-ascii-characters" id="markdown-toc-233-non-ascii-characters">2.3.3 Non-ASCII characters</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li><a href="#3-source-file-structure" id="markdown-toc-3-source-file-structure">3 Source file structure</a>        <ul>
          <li><a href="#31-license-or-copyright-information-if-present" id="markdown-toc-31-license-or-copyright-information-if-present">3.1 License or copyright information, if present</a></li>
          <li><a href="#32-package-declaration" id="markdown-toc-32-package-declaration">3.2 Package declaration</a></li>
          <li><a href="#33-imports" id="markdown-toc-33-imports">3.3 Imports</a>            <ul>
              <li><a href="#331-no-wildcard-imports" id="markdown-toc-331-no-wildcard-imports">3.3.1 No wildcard imports</a></li>
              <li><a href="#3311-no-module-imports" id="markdown-toc-3311-no-module-imports">3.3.1.1 No module imports</a></li>
              <li><a href="#332-no-line-wrapping" id="markdown-toc-332-no-line-wrapping">3.3.2 No line-wrapping</a></li>
              <li><a href="#333-ordering-and-spacing" id="markdown-toc-333-ordering-and-spacing">3.3.3 Ordering and spacing</a></li>
              <li><a href="#334-no-static-import-for-classes" id="markdown-toc-334-no-static-import-for-classes">3.3.4 No static import for classes</a></li>
            </ul>
          </li>
          <li><a href="#34-class-declaration" id="markdown-toc-34-class-declaration">3.4 Class declaration</a>            <ul>
              <li><a href="#341-exactly-one-top-level-class-declaration" id="markdown-toc-341-exactly-one-top-level-class-declaration">3.4.1 Exactly one top-level class declaration</a></li>
              <li><a href="#342-ordering-of-class-contents" id="markdown-toc-342-ordering-of-class-contents">3.4.2 Ordering of class contents</a>                <ul>
                  <li><a href="#3421-overloads-never-split" id="markdown-toc-3421-overloads-never-split">3.4.2.1 Overloads: never split</a></li>
                </ul>
              </li>
            </ul>
          </li>
          <li><a href="#35-module-declaration" id="markdown-toc-35-module-declaration">3.5 Module declaration</a>            <ul>
              <li><a href="#351-ordering-and-spacing-of-module-directives" id="markdown-toc-351-ordering-and-spacing-of-module-directives">3.5.1 Ordering and spacing of module directives</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li><a href="#4-formatting" id="markdown-toc-4-formatting">4 Formatting</a>        <ul>
          <li><a href="#41-braces" id="markdown-toc-41-braces">4.1 Braces</a>            <ul>
              <li><a href="#411-use-of-optional-braces" id="markdown-toc-411-use-of-optional-braces">4.1.1 Use of optional braces</a></li>
              <li><a href="#412-nonempty-blocks-k--r-style" id="markdown-toc-412-nonempty-blocks-k--r-style">4.1.2 Nonempty blocks: K &amp; R style</a></li>
              <li><a href="#413-empty-blocks-may-be-concise" id="markdown-toc-413-empty-blocks-may-be-concise">4.1.3 Empty blocks: may be concise</a></li>
            </ul>
          </li>
          <li><a href="#42-block-indentation-2-spaces" id="markdown-toc-42-block-indentation-2-spaces">4.2 Block indentation: +2 spaces</a></li>
          <li><a href="#43-one-statement-per-line" id="markdown-toc-43-one-statement-per-line">4.3 One statement per line</a></li>
          <li><a href="#44-column-limit-100" id="markdown-toc-44-column-limit-100">4.4 Column limit: 100</a></li>
          <li><a href="#45-line-wrapping" id="markdown-toc-45-line-wrapping">4.5 Line-wrapping</a>            <ul>
              <li><a href="#451-where-to-break" id="markdown-toc-451-where-to-break">4.5.1 Where to break</a></li>
              <li><a href="#452-indent-continuation-lines-at-least-4-spaces" id="markdown-toc-452-indent-continuation-lines-at-least-4-spaces">4.5.2 Indent continuation lines at least +4 spaces</a></li>
            </ul>
          </li>
          <li><a href="#46-whitespace" id="markdown-toc-46-whitespace">4.6 Whitespace</a>            <ul>
              <li><a href="#461-vertical-whitespace-blank-lines" id="markdown-toc-461-vertical-whitespace-blank-lines">4.6.1 Vertical whitespace (blank lines)</a></li>
              <li><a href="#462-horizontal-whitespace" id="markdown-toc-462-horizontal-whitespace">4.6.2 Horizontal whitespace</a></li>
              <li><a href="#463-horizontal-alignment-never-required" id="markdown-toc-463-horizontal-alignment-never-required">4.6.3 Horizontal alignment: never required</a></li>
            </ul>
          </li>
          <li><a href="#47-grouping-parentheses-recommended" id="markdown-toc-47-grouping-parentheses-recommended">4.7 Grouping parentheses: recommended</a></li>
          <li><a href="#48-specific-constructs" id="markdown-toc-48-specific-constructs">4.8 Specific constructs</a>            <ul>
              <li><a href="#481-enum-classes" id="markdown-toc-481-enum-classes">4.8.1 Enum classes</a></li>
              <li><a href="#482-variable-declarations" id="markdown-toc-482-variable-declarations">4.8.2 Variable declarations</a>                <ul>
                  <li><a href="#4821-one-variable-per-declaration" id="markdown-toc-4821-one-variable-per-declaration">4.8.2.1 One variable per declaration</a></li>
                  <li><a href="#4822-declared-when-needed" id="markdown-toc-4822-declared-when-needed">4.8.2.2 Declared when needed</a></li>
                </ul>
              </li>
              <li><a href="#483-arrays" id="markdown-toc-483-arrays">4.8.3 Arrays</a>                <ul>
                  <li><a href="#4831-array-initializers-can-be-block-like" id="markdown-toc-4831-array-initializers-can-be-block-like">4.8.3.1 Array initializers: can be “block-like”</a></li>
                  <li><a href="#4832-no-c-style-array-declarations" id="markdown-toc-4832-no-c-style-array-declarations">4.8.3.2 No C-style array declarations</a></li>
                </ul>
              </li>
              <li><a href="#484-switch-statements-and-expressions" id="markdown-toc-484-switch-statements-and-expressions">4.8.4 Switch statements and expressions</a>                <ul>
                  <li><a href="#4841-indentation" id="markdown-toc-4841-indentation">4.8.4.1 Indentation</a></li>
                  <li><a href="#4842-fall-through-commented" id="markdown-toc-4842-fall-through-commented">4.8.4.2 Fall-through: commented</a></li>
                  <li><a href="#4843-exhaustiveness-and-presence-of-the-default-label" id="markdown-toc-4843-exhaustiveness-and-presence-of-the-default-label">4.8.4.3 Exhaustiveness and presence of the <code class="language-plaintext highlighter-rouge">default</code> label</a></li>
                  <li><a href="#4844-switch-expressions" id="markdown-toc-4844-switch-expressions">4.8.4.4 Switch expressions</a></li>
                </ul>
              </li>
              <li><a href="#485-annotations" id="markdown-toc-485-annotations">4.8.5 Annotations</a>                <ul>
                  <li><a href="#4851-type-use-annotations" id="markdown-toc-4851-type-use-annotations">4.8.5.1 Type-use annotations</a></li>
                  <li><a href="#4852-class-package-and-module-annotations" id="markdown-toc-4852-class-package-and-module-annotations">4.8.5.2 Class, package, and module annotations</a></li>
                  <li><a href="#4853-method-and-constructor-annotations" id="markdown-toc-4853-method-and-constructor-annotations">4.8.5.3 Method and constructor annotations</a></li>
                  <li><a href="#4854-field-annotations" id="markdown-toc-4854-field-annotations">4.8.5.4 Field annotations</a></li>
                  <li><a href="#4855-parameter-and-local-variable-annotations" id="markdown-toc-4855-parameter-and-local-variable-annotations">4.8.5.5 Parameter and local variable annotations</a></li>
                </ul>
              </li>
              <li><a href="#486-comments" id="markdown-toc-486-comments">4.8.6 Comments</a>                <ul>
                  <li><a href="#4861-block-comment-style" id="markdown-toc-4861-block-comment-style">4.8.6.1 Block comment style</a></li>
                  <li><a href="#4862-todo-comments" id="markdown-toc-4862-todo-comments">4.8.6.2 TODO comments</a></li>
                </ul>
              </li>
              <li><a href="#487-modifiers" id="markdown-toc-487-modifiers">4.8.7 Modifiers</a></li>
              <li><a href="#488-numeric-literals" id="markdown-toc-488-numeric-literals">4.8.8 Numeric Literals</a></li>
              <li><a href="#489-text-blocks" id="markdown-toc-489-text-blocks">4.8.9 Text Blocks</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li><a href="#5-naming" id="markdown-toc-5-naming">5 Naming</a>        <ul>
          <li><a href="#51-rules-common-to-all-identifiers" id="markdown-toc-51-rules-common-to-all-identifiers">5.1 Rules common to all identifiers</a></li>
          <li><a href="#52-rules-by-identifier-type" id="markdown-toc-52-rules-by-identifier-type">5.2 Rules by identifier type</a>            <ul>
              <li><a href="#521-package-and-module-names" id="markdown-toc-521-package-and-module-names">5.2.1 Package and module names</a></li>
              <li><a href="#522-class-names" id="markdown-toc-522-class-names">5.2.2 Class names</a></li>
              <li><a href="#523-method-names" id="markdown-toc-523-method-names">5.2.3 Method names</a></li>
              <li><a href="#524-constant-names" id="markdown-toc-524-constant-names">5.2.4 Constant names</a></li>
              <li><a href="#525-non-constant-field-names" id="markdown-toc-525-non-constant-field-names">5.2.5 Non-constant field names</a></li>
              <li><a href="#526-parameter-names" id="markdown-toc-526-parameter-names">5.2.6 Parameter names</a></li>
              <li><a href="#527-local-variable-names" id="markdown-toc-527-local-variable-names">5.2.7 Local variable names</a></li>
              <li><a href="#528-type-variable-names" id="markdown-toc-528-type-variable-names">5.2.8 Type variable names</a></li>
              <li><a href="#529-unnamed-variables" id="markdown-toc-529-unnamed-variables">5.2.9 Unnamed variables</a></li>
            </ul>
          </li>
          <li><a href="#53-camel-case-defined" id="markdown-toc-53-camel-case-defined">5.3 Camel case: defined</a></li>
        </ul>
      </li>
      <li><a href="#6-programming-practices" id="markdown-toc-6-programming-practices">6 Programming Practices</a>        <ul>
          <li><a href="#61-override-always-used" id="markdown-toc-61-override-always-used">6.1 <code class="language-plaintext highlighter-rouge">@Override</code>: always used</a></li>
          <li><a href="#62-caught-exceptions-not-ignored" id="markdown-toc-62-caught-exceptions-not-ignored">6.2 Caught exceptions: not ignored</a></li>
          <li><a href="#63-static-members-qualified-using-class" id="markdown-toc-63-static-members-qualified-using-class">6.3 Static members: qualified using class</a></li>
          <li><a href="#64-finalizers-not-used" id="markdown-toc-64-finalizers-not-used">6.4 Finalizers: not used</a></li>
        </ul>
      </li>
      <li><a href="#7-javadoc" id="markdown-toc-7-javadoc">7 Javadoc</a>        <ul>
          <li><a href="#71-formatting" id="markdown-toc-71-formatting">7.1 Formatting</a>            <ul>
              <li><a href="#711-general-form" id="markdown-toc-711-general-form">7.1.1 General form</a></li>
              <li><a href="#712-paragraphs" id="markdown-toc-712-paragraphs">7.1.2 Paragraphs</a></li>
              <li><a href="#713-block-tags" id="markdown-toc-713-block-tags">7.1.3 Block tags</a></li>
            </ul>
          </li>
          <li><a href="#72-the-summary-fragment" id="markdown-toc-72-the-summary-fragment">7.2 The summary fragment</a></li>
          <li><a href="#73-where-javadoc-is-used" id="markdown-toc-73-where-javadoc-is-used">7.3 Where Javadoc is used</a>            <ul>
              <li><a href="#731-exception-self-explanatory-members" id="markdown-toc-731-exception-self-explanatory-members">7.3.1 Exception: self-explanatory members</a></li>
              <li><a href="#732-exception-overrides" id="markdown-toc-732-exception-overrides">7.3.2 Exception: overrides</a></li>
              <li><a href="#734-non-required-javadoc" id="markdown-toc-734-non-required-javadoc">7.3.4 Non-required Javadoc</a></li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </li>
</ul>
<!-- mdformat on -->

<!-- GitHub pages run markdown through Liquid templating which uses two open
     braces which also shows up in our code examples. Disable parsing for the
     whole document as we don't use Liquid templating anywhere -- the HTML
     conversion is via Kramdown.

     NB: Must come after the [TOC].
      -->

<p><a id="s1-introduction"></a></p>

<h2 id="1-introduction">1 Introduction</h2>

<p>This document serves as the <strong>complete</strong> definition of Google’s coding standards
for source code in the Java™ Programming Language. A Java source file is
described as being <em>in Google Style</em> if and only if it adheres to the rules
herein.</p>

<p>Like other programming style guides, the issues covered span not only aesthetic
issues of formatting, but other types of conventions or coding standards as
well. However, this document focuses primarily on the <strong>hard-and-fast rules</strong>
that we follow universally, and avoids giving <em>advice</em> that isn’t clearly
enforceable (whether by human or tool).</p>

<p><a id="s1.1-terminology"></a></p>

<h3 id="11-terminology-notes">1.1 Terminology notes</h3>

<p>In this document, unless otherwise clarified:</p>

<ol>
  <li>The term <em>class</em> is used inclusively to mean a normal class, record class,
enum class, interface or annotation type (<code class="language-plaintext highlighter-rouge">@interface</code>).</li>
  <li>The term <em>member</em> (of a class) is used inclusively to mean a nested class,
field, method, <em>or constructor</em>; that is, all top-level contents of a class
except initializers.</li>
  <li>The term <em>comment</em> always refers to <em>implementation</em> comments. We do not use
the phrase “documentation comments”, and instead use the common term
“Javadoc.”</li>
</ol>

<p>Other “terminology notes” will appear occasionally throughout the document.</p>

<p><a id="s1.2-guide-notes"></a></p>

<h3 id="12-guide-notes">1.2 Guide notes</h3>

<p>Example code in this document is <strong>non-normative</strong>. That is, while the examples
are in Google Style, they may not illustrate the <em>only</em> stylish way to represent
the code. Optional formatting choices made in examples should not be enforced as
rules.</p>

<p><a id="s2-source-file-basics"></a></p>

<h2 id="2-source-file-basics">2 Source file basics</h2>

<p><a id="s2.1-file-name"></a></p>

<h3 id="21-file-name">2.1 File name</h3>

<p>For a source file containing classes, the file name consists of the
case-sensitive name of the top-level class (of which there is
<a href="#s3.4.1-one-top-level-class">exactly one</a>), plus the <code class="language-plaintext highlighter-rouge">.java</code> extension.</p>

<p><a id="s2.2-file-encoding"></a></p>

<h3 id="22-file-encoding-utf-8">2.2 File encoding: UTF-8</h3>

<p>Source files are encoded in <strong>UTF-8</strong>.</p>

<p><a id="s2.3-special-characters"></a></p>

<h3 id="23-special-characters">2.3 Special characters</h3>

<p><a id="s2.3.1-whitespace-characters"></a></p>

<h4 id="231-whitespace-characters">2.3.1 Whitespace characters</h4>

<p>Aside from the line terminator sequence, the <strong>ASCII horizontal space
character</strong> (<strong>0x20</strong>) is the only whitespace character that appears anywhere in
a source file. This implies that:</p>

<ol>
  <li>All other whitespace characters are escaped in <code class="language-plaintext highlighter-rouge">char</code> and string literals
and in text blocks.</li>
  <li>Tab characters are <strong>not</strong> used for indentation.</li>
</ol>

<p><a id="s2.3.2-special-escape-sequences"></a></p>

<h4 id="232-special-escape-sequences">2.3.2 Special escape sequences</h4>

<p>For any character that has a
<a href="http://docs.oracle.com/javase/tutorial/java/data/characters.html">special escape sequence</a>
(<code class="language-plaintext highlighter-rouge">\b</code>, <code class="language-plaintext highlighter-rouge">\t</code>, <code class="language-plaintext highlighter-rouge">\n</code>, <code class="language-plaintext highlighter-rouge">\f</code>, <code class="language-plaintext highlighter-rouge">\r</code>, <code class="language-plaintext highlighter-rouge">\s</code>, <code class="language-plaintext highlighter-rouge">\"</code>, <code class="language-plaintext highlighter-rouge">\'</code> and <code class="language-plaintext highlighter-rouge">\\ </code>), that sequence is
used rather than the corresponding octal (e.g. <code class="language-plaintext highlighter-rouge">\012</code>) or Unicode (e.g.
<code class="language-plaintext highlighter-rouge">\u000a</code>) escape.</p>

<p><a id="s2.3.3-non-ascii-characters"></a></p>

<h4 id="233-non-ascii-characters">2.3.3 Non-ASCII characters</h4>

<p>For the remaining non-ASCII characters, either the actual Unicode character
(e.g. <code class="language-plaintext highlighter-rouge">∞</code>) or the equivalent Unicode escape (e.g. <code class="language-plaintext highlighter-rouge">\u221e</code>) is used. The choice
depends only on which makes the code <strong>easier to read and understand</strong>, although
Unicode escapes outside string literals and comments are strongly discouraged.</p>

<p><strong>Tip:</strong> In the Unicode escape case, and occasionally even when actual Unicode
characters are used, an explanatory comment can be very helpful.</p>

<p>Examples:</p>

<!-- mdformat off -->

<table>
  <thead>
    <tr>
      <th style="text-align: left">Example</th>
      <th style="text-align: left">Discussion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">String unitAbbrev = "μs";</code></td>
      <td style="text-align: left">Best: perfectly clear even without a comment.</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">String unitAbbrev = "\u03bcs"; // "μs"</code></td>
      <td style="text-align: left">Allowed, but there’s no reason to do this.</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">String unitAbbrev = "\u03bcs"; // Greek letter mu, "s"</code></td>
      <td style="text-align: left">Allowed, but awkward and prone to mistakes.</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">String unitAbbrev = "\u03bcs";</code></td>
      <td style="text-align: left">Poor: the reader has no idea what this is.</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">return '\ufeff' + content; // byte order mark</code></td>
      <td style="text-align: left">Good: use escapes for non-printable characters, and comment if necessary.</td>
    </tr>
  </tbody>
</table>

<!-- mdformat on -->

<p><strong>Tip:</strong> Never make your code less readable simply out of fear that some
programs might not handle non-ASCII characters properly. If that should happen,
those programs are <strong>broken</strong> and they must be <strong>fixed</strong>.</p>

<p><a id="filestructure"></a></p>

<p><a id="s3-source-file-structure"></a></p>

<h2 id="3-source-file-structure">3 Source file structure</h2>

<p>An ordinary source file consists of these sections, <strong>in order</strong>:</p>

<ol>
  <li>License or copyright information, if present</li>
  <li>Package declaration</li>
  <li>Imports</li>
  <li>Exactly one top-level class declaration</li>
</ol>

<p><strong>Exactly one blank line</strong> separates each section that is present.</p>

<p>A <code class="language-plaintext highlighter-rouge">package-info.java</code> file is the same, but without the class declaration.</p>

<p>A <code class="language-plaintext highlighter-rouge">module-info.java</code> file does not contain a package declaration and replaces
the class declaration with a module declaration, but otherwise follows the same
structure.</p>

<p><a id="s3.1-copyright-statement"></a></p>

<h3 id="31-license-or-copyright-information-if-present">3.1 License or copyright information, if present</h3>

<p>If license or copyright information belongs in a file, it belongs here.</p>

<p><a id="s3.2-package-statement"></a> <!-- historical link --></p>

<p><a id="s3.2-package-declaration"></a></p>

<h3 id="32-package-declaration">3.2 Package declaration</h3>

<p>Every source file must have a package declaration.
<a href="https://openjdk.org/jeps/512">Compact source files</a> are not used. (This rule
obviously does not apply to <code class="language-plaintext highlighter-rouge">module-info.java</code> files, which have a different
syntax that does not include a package declaration.)</p>

<p>The package declaration is <strong>not line-wrapped</strong>. The column limit (Section 4.4,
<a href="#s4.4-column-limit">Column limit: 100</a>) does not apply to package declarations.</p>

<p><a id="imports"></a></p>

<p><a id="s3.3-import-statements"></a></p>

<h3 id="33-imports">3.3 Imports</h3>

<p><a id="s3.3.1-wildcard-imports"></a></p>

<h4 id="331-no-wildcard-imports">3.3.1 No wildcard imports</h4>

<p><strong>Wildcard (“on-demand”) imports</strong>, static or otherwise, <strong>are not used</strong>.</p>

<p><a id="s3.3.1.1-module-imports"></a></p>

<h4 id="3311-no-module-imports">3.3.1.1 No module imports</h4>

<p><a href="https://docs.oracle.com/en/java/javase/25/language/module-import-declarations.html">Module imports</a>
<strong>are not used</strong>.</p>

<p>Example:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kn">import</span> <span class="nn">module</span> <span class="n">java</span><span class="o">.</span><span class="na">base</span><span class="o">;</span>
</code></pre></div></div>

<p><a id="s3.3.2-import-line-wrapping"></a></p>

<h4 id="332-no-line-wrapping">3.3.2 No line-wrapping</h4>

<p>Imports are <strong>not line-wrapped</strong>. The column limit (Section 4.4,
<a href="#s4.4-column-limit">Column limit: 100</a>) does not apply to imports.</p>

<p><a id="s3.3.3-import-ordering-and-spacing"></a></p>

<h4 id="333-ordering-and-spacing">3.3.3 Ordering and spacing</h4>

<p>Imports are ordered as follows:</p>

<ol>
  <li>All static imports in a single group.</li>
  <li>All non-static imports in a single group.</li>
</ol>

<p>If there are both static and non-static imports, a single blank line separates
the two groups. There are no other blank lines between imports.</p>

<p>Within each group the imported names appear in ASCII sort order. (<strong>Note:</strong> this
is not the same as the import <em>lines</em> being in ASCII sort order, since ‘.’ sorts
before ‘;’.)</p>

<p><a id="s3.3.4-import-class-not-static"></a></p>

<h4 id="334-no-static-import-for-classes">3.3.4 No static import for classes</h4>

<p>Static import is not used for static nested classes. They are imported with
normal imports.</p>

<p><a id="s3.4-class-declaration"></a></p>

<h3 id="34-class-declaration">3.4 Class declaration</h3>

<p><a id="oneclassperfile"></a></p>

<p><a id="s3.4.1-one-top-level-class"></a></p>

<h4 id="341-exactly-one-top-level-class-declaration">3.4.1 Exactly one top-level class declaration</h4>

<p>Each top-level class resides in a source file of its own.</p>

<p><a id="s3.4.2-class-member-ordering"></a> <!-- historical link --></p>

<p><a id="s3.4.2-ordering-class-contents"></a></p>

<h4 id="342-ordering-of-class-contents">3.4.2 Ordering of class contents</h4>

<p>The order you choose for the members and initializers of your class can have a
great effect on learnability. However, there’s no single correct recipe for how
to do it; different classes may order their contents in different ways.</p>

<p>What is important is that each class uses <strong><em>some</em> logical order</strong>, which its
maintainer could explain if asked. For example, new methods are not just
habitually added to the end of the class, as that would yield “chronological by
date added” ordering, which is not a logical ordering.</p>

<p><a id="overloads"></a></p>

<p><a id="s3.4.2.1-overloads-never-split"></a></p>

<h5 id="3421-overloads-never-split">3.4.2.1 Overloads: never split</h5>

<p>Methods of a class that share the same name appear in a single contiguous group
with no other members in between. The same applies to multiple constructors.
This rule applies even when modifiers such as <code class="language-plaintext highlighter-rouge">static</code> or <code class="language-plaintext highlighter-rouge">private</code> differ
between the methods or constructors.</p>

<p><a id="s3.5-module-declaration"></a></p>

<h3 id="35-module-declaration">3.5 Module declaration</h3>

<p><a id="s3.5.1-ordering-module-directives"></a></p>

<h4 id="351-ordering-and-spacing-of-module-directives">3.5.1 Ordering and spacing of module directives</h4>

<p>Module directives are ordered as follows:</p>

<ol>
  <li>All <code class="language-plaintext highlighter-rouge">requires</code> directives in a single block.</li>
  <li>All <code class="language-plaintext highlighter-rouge">exports</code> directives in a single block.</li>
  <li>All <code class="language-plaintext highlighter-rouge">opens</code> directives in a single block.</li>
  <li>All <code class="language-plaintext highlighter-rouge">uses</code> directives in a single block.</li>
  <li>All <code class="language-plaintext highlighter-rouge">provides</code> directives in a single block.</li>
</ol>

<p>A single blank line separates each block that is present.</p>

<p><a id="s4-formatting"></a></p>

<h2 id="4-formatting">4 Formatting</h2>

<p><strong>Terminology Note:</strong> <em>block-like construct</em> refers to the body of a class,
method, constructor, or switch. Note that, by Section 4.8.3.1 on
<a href="#s4.8.3.1-array-initializers">array initializers</a>, any array initializer <em>may</em>
optionally be treated as if it were a block-like construct.</p>

<p><a id="braces"></a></p>

<p><a id="s4.1-braces"></a></p>

<h3 id="41-braces">4.1 Braces</h3>

<p><a id="s4.1.1-braces-always-used"></a></p>

<h4 id="411-use-of-optional-braces">4.1.1 Use of optional braces</h4>

<p>Braces are used with <code class="language-plaintext highlighter-rouge">if</code>, <code class="language-plaintext highlighter-rouge">else</code>, <code class="language-plaintext highlighter-rouge">for</code>, <code class="language-plaintext highlighter-rouge">do</code> and <code class="language-plaintext highlighter-rouge">while</code> statements, even when
the body is empty or contains only a single statement.</p>

<p>Other optional braces, such as those in a lambda expression, remain optional.</p>

<p><a id="s4.1.2-blocks-k-r-style"></a></p>

<h4 id="412-nonempty-blocks-k--r-style">4.1.2 Nonempty blocks: K &amp; R style</h4>

<p>Braces follow the Kernighan and Ritchie style for <em>nonempty</em> blocks and
block-like constructs:</p>

<ul>
  <li>No line break before the opening brace, except as detailed below.</li>
  <li>Line break after the opening brace.</li>
  <li>Line break before the closing brace.</li>
  <li>Line break after the closing brace, <em>only if</em> that brace terminates a
statement or terminates the body of a method, constructor, or <em>named</em> class.
For example, there is <em>no</em> line break after the brace if it is followed by
<code class="language-plaintext highlighter-rouge">else</code> or a comma.</li>
</ul>

<p>Exception: In places where these rules allow a single statement ending with a
semicolon (<code class="language-plaintext highlighter-rouge">;</code>), a block of statements can appear, and the opening brace of this
block is preceded by a line break. Blocks like these are typically introduced to
limit the scope of local variables.</p>

<p>Examples:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">return</span> <span class="o">()</span> <span class="o">-&gt;</span> <span class="o">{</span>
  <span class="k">while</span> <span class="o">(</span><span class="n">condition</span><span class="o">())</span> <span class="o">{</span>
    <span class="n">method</span><span class="o">();</span>
  <span class="o">}</span>
<span class="o">};</span>

<span class="k">return</span> <span class="k">new</span> <span class="nf">MyClass</span><span class="o">()</span> <span class="o">{</span>
  <span class="nd">@Override</span> <span class="kd">public</span> <span class="kt">void</span> <span class="nf">method</span><span class="o">()</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">condition</span><span class="o">())</span> <span class="o">{</span>
      <span class="k">try</span> <span class="o">{</span>
        <span class="n">something</span><span class="o">();</span>
      <span class="o">}</span> <span class="k">catch</span> <span class="o">(</span><span class="nc">ProblemException</span> <span class="n">e</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">recover</span><span class="o">();</span>
      <span class="o">}</span>
    <span class="o">}</span> <span class="k">else</span> <span class="k">if</span> <span class="o">(</span><span class="n">otherCondition</span><span class="o">())</span> <span class="o">{</span>
      <span class="n">somethingElse</span><span class="o">();</span>
    <span class="o">}</span> <span class="k">else</span> <span class="o">{</span>
      <span class="n">lastThing</span><span class="o">();</span>
    <span class="o">}</span>
    <span class="o">{</span>
      <span class="kt">int</span> <span class="n">x</span> <span class="o">=</span> <span class="n">foo</span><span class="o">();</span>
      <span class="n">frob</span><span class="o">(</span><span class="n">x</span><span class="o">);</span>
    <span class="o">}</span>
  <span class="o">}</span>
<span class="o">};</span>
</code></pre></div></div>

<p>A few exceptions for enum classes are given in Section 4.8.1,
<a href="#s4.8.1-enum-classes">Enum classes</a>.</p>

<p><a id="emptyblocks"></a></p>

<p><a id="s4.1.3-braces-empty-blocks"></a></p>

<h4 id="413-empty-blocks-may-be-concise">4.1.3 Empty blocks: may be concise</h4>

<p>An empty block or block-like construct may be in K &amp; R style (as described in
<a href="#s4.1.2-blocks-k-r-style">Section 4.1.2</a>). Alternatively, it may be closed
immediately after it is opened, with no characters or line break in between
(<code class="language-plaintext highlighter-rouge">{}</code>), <strong>unless</strong> it is part of a <em>multi-block statement</em> (one that directly
contains multiple blocks: <code class="language-plaintext highlighter-rouge">if/else</code> or <code class="language-plaintext highlighter-rouge">try/catch/finally</code>).</p>

<p>Examples:</p>

<div class="goodcode"></div>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code>  <span class="c1">// This is acceptable</span>
  <span class="kt">void</span> <span class="nf">doNothing</span><span class="o">()</span> <span class="o">{}</span>

  <span class="c1">// This is equally acceptable</span>
  <span class="kt">void</span> <span class="nf">doNothingElse</span><span class="o">()</span> <span class="o">{</span>
  <span class="o">}</span>
</code></pre></div></div>

<div class="badcode"></div>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code>  <span class="c1">// This is not acceptable: No concise empty blocks in a multi-block statement</span>
  <span class="k">try</span> <span class="o">{</span>
    <span class="n">doSomething</span><span class="o">();</span>
  <span class="o">}</span> <span class="k">catch</span> <span class="o">(</span><span class="nc">Exception</span> <span class="n">e</span><span class="o">)</span> <span class="o">{}</span>
</code></pre></div></div>

<p><a id="s4.2-block-indentation"></a></p>

<h3 id="42-block-indentation-2-spaces">4.2 Block indentation: +2 spaces</h3>

<p>Each time a new block or block-like construct is opened, the indent increases by
two spaces. When the block ends, the indent returns to the previous indent
level. The indent level applies to both code and comments throughout the block.
(See the example in Section 4.1.2,
<a href="#s4.1.2-blocks-k-r-style">Nonempty blocks: K &amp; R Style</a>.)</p>

<p><a id="s4.3-one-statement-per-line"></a></p>

<h3 id="43-one-statement-per-line">4.3 One statement per line</h3>

<p>Each statement is followed by a line break.</p>

<p><a id="columnlimit"></a></p>

<p><a id="s4.4-column-limit"></a></p>

<h3 id="44-column-limit-100">4.4 Column limit: 100</h3>

<p>Java code has a column limit of 100 characters. A “character” means any Unicode
code point. Except as noted below, any line that would exceed this limit must be
line-wrapped, as explained in Section 4.5, <a href="#s4.5-line-wrapping">Line-wrapping</a>.</p>

<p><strong>Tip:</strong> Each Unicode code point counts as one character, even if its display
width is greater or less. For example, if using
<a href="https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms">fullwidth characters</a>,
you may choose to wrap the line earlier than where this rule strictly requires.</p>

<p><strong>Exceptions:</strong></p>

<ol>
  <li>Lines where obeying the column limit is not possible (for example, a long
URL in Javadoc, or a long JSNI method reference).</li>
  <li><code class="language-plaintext highlighter-rouge">package</code> declarations and imports (see Sections 3.2
<a href="#s3.2-package-statement">Package declarations</a> and 3.3
<a href="#s3.3-import-statements">Imports</a>).</li>
  <li>Contents of <a href="#s4.8.9-text-blocks">text blocks</a>.</li>
  <li>Command lines in a comment that may be copied-and-pasted into a shell.</li>
  <li>Very long identifiers, on the rare occasions they are called for, are
allowed to exceed the column limit. In that case, the valid wrapping for the
surrounding code is as produced by
<a href="https://github.com/google/google-java-format">google-java-format</a>.</li>
</ol>

<p><a id="s4.5-line-wrapping"></a></p>

<h3 id="45-line-wrapping">4.5 Line-wrapping</h3>

<p><strong>Terminology Note:</strong> When code that might otherwise occupy a single line is
divided into multiple lines, this activity is called <em>line-wrapping</em>.</p>

<p>There is no comprehensive, deterministic formula showing <em>exactly</em> how to
line-wrap in every situation. Very often there are several valid ways to
line-wrap the same piece of code.</p>

<p><strong>Note:</strong> While the typical reason for line-wrapping is to avoid overflowing the
column limit, even code that would in fact fit within the column limit <em>may</em> be
line-wrapped at the author’s discretion.</p>

<p><strong>Tip:</strong> Extracting a method or local variable may solve the problem without the
need to line-wrap.</p>

<p><a id="s4.5.1-line-wrapping-where-to-break"></a></p>

<h4 id="451-where-to-break">4.5.1 Where to break</h4>

<p>The prime directive of line-wrapping is: prefer to break at a <strong>higher syntactic
level</strong>. Also:</p>

<ol>
  <li>
    <p>When a line is broken at a <em>non-assignment</em> operator the break comes
<em>before</em> the symbol. (Note that this is not the same practice used in Google
style for other languages, such as C++ and JavaScript.)</p>

    <ul>
      <li>
        <p>This also applies to the following “operator-like” symbols:</p>

        <ul>
          <li>the dot separator (<code class="language-plaintext highlighter-rouge">.</code>)</li>
          <li>the two colons of a method reference (<code class="language-plaintext highlighter-rouge">::</code>)</li>
          <li>an ampersand in a type bound (<code class="language-plaintext highlighter-rouge">&lt;T extends Foo &amp; Bar&gt;</code>)</li>
          <li>a pipe in a catch block (<code class="language-plaintext highlighter-rouge">catch (FooException | BarException e)</code>).</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    <p>When a line is broken at an <em>assignment</em> operator the break typically comes
<em>after</em> the symbol, but either way is acceptable.</p>

    <ul>
      <li>This also applies to the colon in an enhanced <code class="language-plaintext highlighter-rouge">for</code> (“foreach”)
statement.</li>
    </ul>
  </li>
  <li>
    <p>A method, constructor, or record-class name stays attached to the open
parenthesis (<code class="language-plaintext highlighter-rouge">(</code>) that follows it.</p>
  </li>
  <li>
    <p>A comma (<code class="language-plaintext highlighter-rouge">,</code>) stays attached to the token that precedes it.</p>
  </li>
  <li>
    <p>A line is never broken adjacent to the arrow in a lambda or a switch rule,
except that a break may come immediately after the arrow if the text
following it consists of a single unbraced expression. Examples:</p>

    <div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nc">MyLambda</span><span class="o">&lt;</span><span class="nc">String</span><span class="o">,</span> <span class="nc">Long</span><span class="o">,</span> <span class="nc">Object</span><span class="o">&gt;</span> <span class="n">lambda</span> <span class="o">=</span>
    <span class="o">(</span><span class="nc">String</span> <span class="n">label</span><span class="o">,</span> <span class="nc">Long</span> <span class="n">value</span><span class="o">,</span> <span class="nc">Object</span> <span class="n">obj</span><span class="o">)</span> <span class="o">-&gt;</span> <span class="o">{</span>
      <span class="o">...</span>
    <span class="o">};</span>

<span class="nc">Predicate</span><span class="o">&lt;</span><span class="nc">String</span><span class="o">&gt;</span> <span class="n">predicate</span> <span class="o">=</span> <span class="n">str</span> <span class="o">-&gt;</span>
    <span class="n">longExpressionInvolving</span><span class="o">(</span><span class="n">str</span><span class="o">);</span>

<span class="k">switch</span> <span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="o">{</span>
  <span class="k">case</span> <span class="nf">ColorPoint</span><span class="o">(</span><span class="nc">Color</span> <span class="n">color</span><span class="o">,</span> <span class="nc">Point</span><span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">,</span> <span class="kt">int</span> <span class="n">y</span><span class="o">))</span> <span class="o">-&gt;</span>
      <span class="n">handleColorPoint</span><span class="o">(</span><span class="n">color</span><span class="o">,</span> <span class="n">x</span><span class="o">,</span> <span class="n">y</span><span class="o">);</span>
  <span class="o">...</span>
<span class="o">}</span>
</code></pre></div>    </div>
  </li>
</ol>

<p><strong>Note:</strong> The primary goal for line wrapping is to have clear code, <em>not
necessarily</em> code that fits in the smallest number of lines.</p>

<p><a id="indentation"></a></p>

<p><a id="s4.5.2-line-wrapping-indent"></a></p>

<h4 id="452-indent-continuation-lines-at-least-4-spaces">4.5.2 Indent continuation lines at least +4 spaces</h4>

<p>When line-wrapping, each line after the first (each <em>continuation line</em>) is
indented at least +4 from the original line.</p>

<p>When there are multiple continuation lines, indentation may be varied beyond +4
as desired. In general, two continuation lines use the same indentation level if
and only if they begin with syntactically parallel elements.</p>

<p>Section 4.6.3 on <a href="#s4.6.3-horizontal-alignment">Horizontal alignment</a> addresses
the discouraged practice of using a variable number of spaces to align certain
tokens with previous lines.</p>

<p><a id="s4.6-whitespace"></a></p>

<h3 id="46-whitespace">4.6 Whitespace</h3>

<p><a id="s4.6.1-vertical-whitespace"></a></p>

<h4 id="461-vertical-whitespace-blank-lines">4.6.1 Vertical whitespace (blank lines)</h4>

<p>A single blank line always appears:</p>

<ol>
  <li>
    <p><em>Between</em> consecutive members or initializers of a class: fields,
constructors, methods, nested classes, static initializers, and instance
initializers.</p>

    <ul>
      <li><strong>Exception:</strong> A blank line between two consecutive fields (having no
other code between them) is optional. Such blank lines are used as
needed to create <em>logical groupings</em> of fields.</li>
      <li><strong>Exception:</strong> Blank lines between enum constants are covered in
<a href="#s4.8.1-enum-classes">Section 4.8.1</a>.</li>
    </ul>
  </li>
  <li>
    <p>As required by other sections of this document (such as Section 3,
<a href="#s3-source-file-structure">Source file structure</a>, and Section 3.3,
<a href="#s3.3-import-statements">Imports</a>).</p>
  </li>
</ol>

<p>A single blank line may also appear anywhere it improves readability, for
example between statements to organize the code into logical subsections. A
blank line before the first member or initializer, or after the last member or
initializer of the class, is neither encouraged nor discouraged.</p>

<p><em>Multiple</em> consecutive blank lines are permitted, but never required (or
encouraged).</p>

<p><a id="s4.6.2-horizontal-whitespace"></a></p>

<h4 id="462-horizontal-whitespace">4.6.2 Horizontal whitespace</h4>

<p>Beyond where required by the language or other style rules, and apart from
within literals, comments and Javadoc, a single ASCII space also appears in the
following places <strong>only</strong>.</p>

<ol>
  <li>
    <p>Separating any keyword, such as <code class="language-plaintext highlighter-rouge">if</code>, <code class="language-plaintext highlighter-rouge">for</code> or <code class="language-plaintext highlighter-rouge">catch</code>, from an open
parenthesis (<code class="language-plaintext highlighter-rouge">(</code>) that follows it on that line</p>
  </li>
  <li>
    <p>Separating any keyword, such as <code class="language-plaintext highlighter-rouge">else</code> or <code class="language-plaintext highlighter-rouge">catch</code>, from a closing curly
brace (<code class="language-plaintext highlighter-rouge">}</code>) that precedes it on that line</p>
  </li>
  <li>
    <p>Before any open curly brace (<code class="language-plaintext highlighter-rouge">{</code>), with two exceptions:</p>

    <ul>
      <li><code class="language-plaintext highlighter-rouge">@SomeAnnotation({a, b})</code> (no space is used)</li>
      <li><code class="language-plaintext highlighter-rouge">String[][] x = {{"foo"}};</code> (no space is required between <code class="language-plaintext highlighter-rouge">{{</code>, by item
10 below)</li>
    </ul>
  </li>
  <li>
    <p>On both sides of any binary or ternary operator. This also applies to the
following “operator-like” symbols:</p>

    <ul>
      <li>the ampersand that separates multiple type bounds:
<code class="language-plaintext highlighter-rouge">&lt;T extends Foo &amp; Bar&gt;</code></li>
      <li>the pipe for a catch block that handles multiple exceptions:
<code class="language-plaintext highlighter-rouge">catch (FooException | BarException e)</code></li>
      <li>the colon (<code class="language-plaintext highlighter-rouge">:</code>) in an enhanced <code class="language-plaintext highlighter-rouge">for</code> (“foreach”) statement</li>
      <li>the arrow in a lambda expression: <code class="language-plaintext highlighter-rouge">(String str) -&gt; str.length()</code> <br />
or switch rule: <code class="language-plaintext highlighter-rouge">case "FOO" -&gt; bar();</code></li>
    </ul>

    <p>but not</p>

    <ul>
      <li>the two colons (<code class="language-plaintext highlighter-rouge">::</code>) of a method reference, which is written like
<code class="language-plaintext highlighter-rouge">Object::toString</code></li>
      <li>the dot separator (<code class="language-plaintext highlighter-rouge">.</code>), which is written like <code class="language-plaintext highlighter-rouge">object.toString()</code></li>
    </ul>
  </li>
  <li>
    <p>After <code class="language-plaintext highlighter-rouge">,:;</code> or the closing parenthesis (<code class="language-plaintext highlighter-rouge">)</code>) of a cast</p>
  </li>
  <li>
    <p>Between any content and a double slash (<code class="language-plaintext highlighter-rouge">//</code>) which begins a comment.
Multiple spaces are allowed.</p>
  </li>
  <li>
    <p>Between a double slash (<code class="language-plaintext highlighter-rouge">//</code>) which begins a comment and the comment’s text.
Multiple spaces are allowed.</p>
  </li>
  <li>
    <p>Between the type and identifier of a declaration: <code class="language-plaintext highlighter-rouge">List&lt;String&gt; list</code></p>
  </li>
  <li>
    <p><em>Optional</em> just inside both braces of an array initializer</p>

    <ul>
      <li><code class="language-plaintext highlighter-rouge">new int[] {5, 6}</code> and <code class="language-plaintext highlighter-rouge">new int[] { 5, 6 }</code> are both valid</li>
    </ul>
  </li>
  <li>
    <p>Between a type annotation and <code class="language-plaintext highlighter-rouge">[]</code> or <code class="language-plaintext highlighter-rouge">...</code>.</p>
  </li>
</ol>

<p>This rule is never interpreted as requiring or forbidding additional space at
the start or end of a line; it addresses only <em>interior</em> space.</p>

<p><a id="s4.6.3-horizontal-alignment"></a></p>

<h4 id="463-horizontal-alignment-never-required">4.6.3 Horizontal alignment: never required</h4>

<p><strong>Terminology Note:</strong> <em>Horizontal alignment</em> is the practice of adding a
variable number of additional spaces in your code with the goal of making
certain tokens appear directly below certain other tokens on previous lines.</p>

<p>This practice is permitted, but is <strong>never required</strong> by Google Style. It is not
even required to <em>maintain</em> horizontal alignment in places where it was already
used.</p>

<p>Here is an example without alignment, then using alignment:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kd">private</span> <span class="kt">int</span> <span class="n">x</span><span class="o">;</span> <span class="c1">// this is fine</span>
<span class="kd">private</span> <span class="nc">Color</span> <span class="n">color</span><span class="o">;</span> <span class="c1">// this too</span>

<span class="kd">private</span> <span class="kt">int</span>   <span class="n">x</span><span class="o">;</span>      <span class="c1">// permitted, but future edits</span>
<span class="kd">private</span> <span class="nc">Color</span> <span class="n">color</span><span class="o">;</span>  <span class="c1">// may leave it unaligned</span>
</code></pre></div></div>

<p><strong>Tip:</strong> Alignment can aid readability, but attempting to preserve alignment for
its own sake creates future problems. For example, consider a change that
touches only one line. If that change disrupts the previous alignment, it’s
important <strong>not</strong> to introduce additional changes on nearby lines simply to
realign them. Introducing formatting changes on otherwise unaffected lines
corrupts version history, slows down reviewers, and exacerbates merge conflicts.
These practical concerns take priority over alignment.</p>

<p><a id="parentheses"></a></p>

<p><a id="s4.7-grouping-parentheses"></a></p>

<h3 id="47-grouping-parentheses-recommended">4.7 Grouping parentheses: recommended</h3>

<p>Optional grouping parentheses are omitted only when author and reviewer agree
that there is no reasonable chance the code will be misinterpreted without them,
nor would they have made the code easier to read. It is <em>not</em> reasonable to
assume that every reader has the entire Java operator precedence table
memorized.</p>

<p><a id="s4.8-specific-constructs"></a></p>

<h3 id="48-specific-constructs">4.8 Specific constructs</h3>

<p><a id="s4.8.1-enum-classes"></a></p>

<h4 id="481-enum-classes">4.8.1 Enum classes</h4>

<p>After the comma that follows an enum constant, a line break is optional.
Additional blank lines (usually just one) are also allowed. This is one
possibility:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kd">private</span> <span class="kd">enum</span> <span class="nc">Answer</span> <span class="o">{</span>
  <span class="no">YES</span> <span class="o">{</span>
    <span class="nd">@Override</span> <span class="kd">public</span> <span class="nc">String</span> <span class="nf">toString</span><span class="o">()</span> <span class="o">{</span>
      <span class="k">return</span> <span class="s">"yes"</span><span class="o">;</span>
    <span class="o">}</span>
  <span class="o">},</span>

  <span class="no">NO</span><span class="o">,</span>
  <span class="no">MAYBE</span>
<span class="o">}</span>
</code></pre></div></div>

<p>An enum class with no methods and no documentation on its constants may
optionally be formatted as if it were an array initializer (see Section 4.8.3.1
on <a href="#s4.8.3.1-array-initializers">array initializers</a>).</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kd">private</span> <span class="kd">enum</span> <span class="nc">Suit</span> <span class="o">{</span> <span class="no">CLUBS</span><span class="o">,</span> <span class="no">HEARTS</span><span class="o">,</span> <span class="no">SPADES</span><span class="o">,</span> <span class="no">DIAMONDS</span> <span class="o">}</span>
</code></pre></div></div>

<p>Since enum classes <em>are classes</em>, all other rules for formatting classes apply.</p>

<p><a id="localvariables"></a></p>

<p><a id="s4.8.2-variable-declarations"></a></p>

<h4 id="482-variable-declarations">4.8.2 Variable declarations</h4>

<p><a id="s4.8.2.1-variables-per-declaration"></a></p>

<h5 id="4821-one-variable-per-declaration">4.8.2.1 One variable per declaration</h5>

<p>Every variable declaration (field or local) declares only one variable:
declarations such as <code class="language-plaintext highlighter-rouge">int a, b;</code> are not used.</p>

<p><strong>Exception:</strong> Multiple variable declarations are acceptable in the header of a
<code class="language-plaintext highlighter-rouge">for</code> loop.</p>

<p><a id="s4.8.2.2-variables-limited-scope"></a></p>

<h5 id="4822-declared-when-needed">4.8.2.2 Declared when needed</h5>

<p>Local variables are <strong>not</strong> habitually declared at the start of their containing
block or block-like construct. Instead, local variables are declared close to
the point they are first used (within reason), to minimize their scope. Local
variable declarations typically have initializers, or are initialized
immediately after declaration.</p>

<p><a id="s4.8.3-arrays"></a></p>

<h4 id="483-arrays">4.8.3 Arrays</h4>

<p><a id="s4.8.3.1-array-initializers"></a></p>

<h5 id="4831-array-initializers-can-be-block-like">4.8.3.1 Array initializers: can be “block-like”</h5>

<p>Any array initializer may <em>optionally</em> be formatted as if it were a “block-like
construct.” For example, the following are all valid (<strong>not</strong> an exhaustive
list):</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">new</span> <span class="kt">int</span><span class="o">[]</span> <span class="o">{</span>           <span class="k">new</span> <span class="kt">int</span><span class="o">[]</span> <span class="o">{</span>
  <span class="mi">0</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">3</span>            <span class="mi">0</span><span class="o">,</span>
<span class="o">}</span>                       <span class="mi">1</span><span class="o">,</span>
                        <span class="mi">2</span><span class="o">,</span>
<span class="k">new</span> <span class="kt">int</span><span class="o">[]</span> <span class="o">{</span>             <span class="mi">3</span><span class="o">,</span>
  <span class="mi">0</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span>               <span class="o">}</span>
  <span class="mi">2</span><span class="o">,</span> <span class="mi">3</span>
<span class="o">}</span>                     <span class="k">new</span> <span class="kt">int</span><span class="o">[]</span>
                          <span class="o">{</span><span class="mi">0</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">3</span><span class="o">}</span>
</code></pre></div></div>

<p><a id="s4.8.3.2-array-declarations"></a></p>

<h5 id="4832-no-c-style-array-declarations">4.8.3.2 No C-style array declarations</h5>

<p>The square brackets form a part of the <em>type</em>, not the variable:
<code class="language-plaintext highlighter-rouge">String[] args</code>, not <code class="language-plaintext highlighter-rouge">String args[]</code>.</p>

<p><a id="s4.8.4-switch"></a></p>

<h4 id="484-switch-statements-and-expressions">4.8.4 Switch statements and expressions</h4>

<p>For historical reasons, the Java language has two distinct syntaxes for
<code class="language-plaintext highlighter-rouge">switch</code>, which we can call <em>old-style</em> and <em>new-style</em>. New-style switches use
an arrow (<code class="language-plaintext highlighter-rouge">-&gt;</code>) after the switch labels, while old-style switches use a colon
(<code class="language-plaintext highlighter-rouge">:</code>).</p>

<p><strong>Terminology Note:</strong> Inside the braces of a <em>switch block</em> are either one or
more <em>switch rules</em> (new-style); or one or more <em>statement groups</em> (old-style).
A <em>switch rule</em> consists of a <em>switch label</em> (<code class="language-plaintext highlighter-rouge">case ...</code> or <code class="language-plaintext highlighter-rouge">default</code>) followed
by <code class="language-plaintext highlighter-rouge">-&gt;</code> and an expression, block, or <code class="language-plaintext highlighter-rouge">throw</code>. A statement group consists of one
or more switch labels each followed by a colon, then one or more statements, or,
for the <em>last</em> statement group, <em>zero</em> or more statements. (These definitions
match the Java Language Specification,
<a href="https://docs.oracle.com/javase/specs/jls/se21/html/jls-14.html#jls-14.11">§14.11</a>.)</p>

<p><a id="s4.8.4.1-switch-indentation"></a></p>

<h5 id="4841-indentation">4.8.4.1 Indentation</h5>

<p>As with any other block, the contents of a switch block are indented +2. Each
switch label starts with this +2 indentation.</p>

<p>In a new-style switch, a switch rule can be written on a single line if it
otherwise follows Google style. (It must not exceed the column limit, and if it
contains a non-empty block then there must be a line break after <code class="language-plaintext highlighter-rouge">{</code>.) The
line-wrapping rules of <a href="#s4.5-line-wrapping">Section 4.5</a> apply, including the
+4 indent for continuation lines. For a switch rule with a non-empty block after
the arrow, the same rules apply as for blocks elsewhere: lines between <code class="language-plaintext highlighter-rouge">{</code> and
<code class="language-plaintext highlighter-rouge">}</code> are indented a further +2 relative to the line with the switch label.</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">switch</span> <span class="o">(</span><span class="n">number</span><span class="o">)</span> <span class="o">{</span>
  <span class="k">case</span> <span class="mi">0</span><span class="o">,</span> <span class="mi">1</span> <span class="o">-&gt;</span> <span class="n">handleZeroOrOne</span><span class="o">();</span>
  <span class="k">case</span> <span class="mi">2</span> <span class="o">-&gt;</span>
      <span class="n">handleTwoWithAnExtremelyLongMethodCallThatWouldNotFitOnTheSameLine</span><span class="o">();</span>
  <span class="k">default</span> <span class="o">-&gt;</span> <span class="o">{</span>
    <span class="n">logger</span><span class="o">.</span><span class="na">atInfo</span><span class="o">().</span><span class="na">log</span><span class="o">(</span><span class="s">"Surprising number %s"</span><span class="o">,</span> <span class="n">number</span><span class="o">);</span>
    <span class="n">handleSurprisingNumber</span><span class="o">(</span><span class="n">number</span><span class="o">);</span>
  <span class="o">}</span>
<span class="o">}</span>
</code></pre></div></div>

<p>In an old-style switch, the colon of each switch label is followed by a line
break. The statements within a statement group are indented a further +2.</p>

<p><a id="fallthrough"></a></p>

<p><a id="s4.8.4.2-switch-fall-through"></a></p>

<h5 id="4842-fall-through-commented">4.8.4.2 Fall-through: commented</h5>

<p>Within an old-style switch block, each statement group either terminates
abruptly (with a <code class="language-plaintext highlighter-rouge">break</code>, <code class="language-plaintext highlighter-rouge">continue</code>, <code class="language-plaintext highlighter-rouge">return</code> or thrown exception), or is
marked with a comment to indicate that execution will or <em>might</em> continue into
the next statement group. Any comment that communicates the idea of fall-through
is sufficient (typically <code class="language-plaintext highlighter-rouge">// fall through</code>). This special comment is not
required in the last statement group of the switch block. Example:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">switch</span> <span class="o">(</span><span class="n">input</span><span class="o">)</span> <span class="o">{</span>
  <span class="k">case</span> <span class="mi">1</span><span class="o">:</span>
  <span class="k">case</span> <span class="mi">2</span><span class="o">:</span>
    <span class="n">prepareOneOrTwo</span><span class="o">();</span>
  <span class="c1">// fall through</span>
  <span class="k">case</span> <span class="mi">3</span><span class="o">:</span>
    <span class="n">handleOneTwoOrThree</span><span class="o">();</span>
    <span class="k">break</span><span class="o">;</span>
  <span class="k">default</span><span class="o">:</span>
    <span class="n">handleLargeNumber</span><span class="o">(</span><span class="n">input</span><span class="o">);</span>
<span class="o">}</span>
</code></pre></div></div>

<p>Notice that no comment is needed after <code class="language-plaintext highlighter-rouge">case 1:</code>, only at the end of the
statement group.</p>

<p>There is no fall-through in new-style switches.</p>

<p><a id="s4.8.4.3-switch-default"></a></p>

<h5 id="4843-exhaustiveness-and-presence-of-the-default-label">4.8.4.3 Exhaustiveness and presence of the <code class="language-plaintext highlighter-rouge">default</code> label</h5>

<p>The Java language requires switch expressions and many kinds of switch
statements to be <em>exhaustive</em>. That effectively means that every possible value
that could be switched on will be matched by one of the switch labels. A switch
is exhaustive if it has a <code class="language-plaintext highlighter-rouge">default</code> label, but also for example if the value
being switched on is an enum and every value of the enum is matched by a switch
label. Google Style requires <em>every</em> switch to be exhaustive, even those where
the language itself does not require it. This may require adding a <code class="language-plaintext highlighter-rouge">default</code>
label, even if it contains no code.</p>

<p><a id="s4.8.4.4-switch-expressions"></a></p>

<h5 id="4844-switch-expressions">4.8.4.4 Switch expressions</h5>

<p>Switch expressions must be new-style switches:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code>  <span class="k">return</span> <span class="k">switch</span> <span class="o">(</span><span class="n">list</span><span class="o">.</span><span class="na">size</span><span class="o">())</span> <span class="o">{</span>
    <span class="k">case</span> <span class="mi">0</span> <span class="o">-&gt;</span> <span class="s">""</span><span class="o">;</span>
    <span class="k">case</span> <span class="mi">1</span> <span class="o">-&gt;</span> <span class="n">list</span><span class="o">.</span><span class="na">getFirst</span><span class="o">();</span>
    <span class="k">default</span> <span class="o">-&gt;</span> <span class="nc">String</span><span class="o">.</span><span class="na">join</span><span class="o">(</span><span class="s">", "</span><span class="o">,</span> <span class="n">list</span><span class="o">);</span>
  <span class="o">};</span>
</code></pre></div></div>

<p><a id="annotations"></a></p>

<p><a id="s4.8.5-annotations"></a></p>

<h4 id="485-annotations">4.8.5 Annotations</h4>

<p><a id="s4.8.5.1-type-use-annotation-style"></a></p>

<h5 id="4851-type-use-annotations">4.8.5.1 Type-use annotations</h5>

<p>Type-use annotations appear immediately before the annotated type. An annotation
is a type-use annotation if it is meta-annotated with
<code class="language-plaintext highlighter-rouge">@Target(ElementType.TYPE_USE)</code>. Example:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kd">final</span> <span class="nd">@Nullable</span> <span class="nc">String</span> <span class="n">name</span><span class="o">;</span>

<span class="kd">public</span> <span class="nd">@Nullable</span> <span class="nc">Person</span> <span class="nf">getPersonByName</span><span class="o">(</span><span class="nc">String</span> <span class="n">name</span><span class="o">);</span>
</code></pre></div></div>

<p><a id="s4.8.5.2-class-annotation-style"></a></p>

<h5 id="4852-class-package-and-module-annotations">4.8.5.2 Class, package, and module annotations</h5>

<p>Annotations applying to a class, package, or module declaration appear
immediately after the documentation block, and each annotation is listed on a
line of its own (that is, one annotation per line). These line breaks do not
constitute line-wrapping (Section 4.5, <a href="#s4.5-line-wrapping">Line-wrapping</a>), so
the indentation level is not increased. Examples:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">/// This is a class.</span>
<span class="nd">@Deprecated</span>
<span class="nd">@CheckReturnValue</span>
<span class="kd">public</span> <span class="kd">final</span> <span class="kd">class</span> <span class="nc">Frozzler</span> <span class="o">{</span> <span class="o">...</span> <span class="o">}</span>
</code></pre></div></div>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">/// This is a package.</span>
<span class="nd">@Deprecated</span>
<span class="nd">@CheckReturnValue</span>
<span class="kn">package</span> <span class="nn">com.example.frozzler</span><span class="o">;</span>
</code></pre></div></div>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">/// This is a module.</span>
<span class="nd">@Deprecated</span>
<span class="nd">@SuppressWarnings</span><span class="o">(</span><span class="s">"CheckReturnValue"</span><span class="o">)</span> <span class="c1">// TODO(b/12345): Fix existing CRV violations.</span>
<span class="n">module</span> <span class="n">com</span><span class="o">.</span><span class="na">example</span><span class="o">.</span><span class="na">frozzler</span> <span class="o">{</span> <span class="o">...</span> <span class="o">}</span>
</code></pre></div></div>

<p><a id="s4.8.5.3-method-annotation-style"></a></p>

<h5 id="4853-method-and-constructor-annotations">4.8.5.3 Method and constructor annotations</h5>

<p>The rules for annotations on method and constructor declarations are the same as
the <a href="#s4.8.5.2-class-annotation-style">previous section</a>. Example:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nd">@Deprecated</span>
<span class="nd">@Override</span>
<span class="kd">public</span> <span class="nc">String</span> <span class="nf">getNameIfPresent</span><span class="o">()</span> <span class="o">{</span> <span class="o">...</span> <span class="o">}</span>
</code></pre></div></div>

<p><strong>Exception:</strong> If the method or constructor only has a <em>single</em>, <em>parameterless</em>
annotation, it <em>may</em> appear together with the first line of the signature, for
example:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nd">@Override</span> <span class="kd">public</span> <span class="kt">int</span> <span class="nf">hashCode</span><span class="o">()</span> <span class="o">{</span> <span class="o">...</span> <span class="o">}</span>
</code></pre></div></div>

<p><a id="s4.8.5.4-field-annotation-style"></a></p>

<h5 id="4854-field-annotations">4.8.5.4 Field annotations</h5>

<p>Annotations applying to a field also appear immediately after the documentation
block, but in this case, <em>multiple</em> annotations (possibly parameterized) may be
listed on the same line; for example:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nd">@Partial</span> <span class="nd">@Mock</span> <span class="nc">DataLoader</span> <span class="n">loader</span><span class="o">;</span>
</code></pre></div></div>

<p><a id="s4.8.5.5-local-parameter-annotation-style"></a></p>

<h5 id="4855-parameter-and-local-variable-annotations">4.8.5.5 Parameter and local variable annotations</h5>

<p>There are no specific rules for formatting annotations on parameters or local
variables (except, of course, when the annotation is a type-use annotation).</p>

<p><a id="comments"></a></p>

<p><a id="s4.8.6-comments"></a></p>

<h4 id="486-comments">4.8.6 Comments</h4>

<p>This section addresses <em>implementation comments</em>. Javadoc is addressed
separately in Section 7, <a href="#s7-javadoc">Javadoc</a>.</p>

<p>Any line break may be preceded by arbitrary whitespace followed by an
implementation comment. Such a comment renders the line non-blank.</p>

<p><a id="s4.8.6.1-block-comment-style"></a></p>

<h5 id="4861-block-comment-style">4.8.6.1 Block comment style</h5>

<p>Block comments are indented at the same level as the surrounding code. They may
be in <code class="language-plaintext highlighter-rouge">/* ... */</code> style or <code class="language-plaintext highlighter-rouge">// ...</code> style. For multi-line <code class="language-plaintext highlighter-rouge">/* ... */</code> comments,
subsequent lines must start with <code class="language-plaintext highlighter-rouge">*</code> aligned with the <code class="language-plaintext highlighter-rouge">*</code> on the previous line.</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cm">/*
 * This is          // And so           /* Or you can
 * okay.            // is this.          * even do this. */</span>
 <span class="o">*/</span>
</code></pre></div></div>

<p>Comments are not enclosed in boxes drawn with asterisks or other characters.</p>

<p><strong>Tip:</strong> When writing multi-line comments, use the <code class="language-plaintext highlighter-rouge">/* ... */</code> style if you want
automatic code formatters to re-wrap the lines when necessary (paragraph-style).
Most formatters don’t re-wrap lines in <code class="language-plaintext highlighter-rouge">// ...</code> style comment blocks.</p>

<p><a id="todo"></a></p>

<p><a id="s4.8.6.2-todo-comments"></a></p>

<h5 id="4862-todo-comments">4.8.6.2 TODO comments</h5>

<p>Use <code class="language-plaintext highlighter-rouge">TODO</code> comments for code that is temporary, a short-term solution, or
good-enough but not perfect.</p>

<p>A <code class="language-plaintext highlighter-rouge">TODO</code> comment begins with the word <code class="language-plaintext highlighter-rouge">TODO</code> in all caps, a following colon, and
a link to a resource that contains the context, ideally a bug reference. A bug
reference is preferable because bugs are tracked and have follow-up comments.
Follow this piece of context with an explanatory string introduced with a hyphen
<code class="language-plaintext highlighter-rouge">-</code>.</p>

<p>The purpose is to have a consistent <code class="language-plaintext highlighter-rouge">TODO</code> format that can be searched to find
out how to get more details.</p>

<div class="goodcode"></div>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">// TODO: example.com/12345678 - Remove this after the 2047q4 compatibility window expires.</span>
</code></pre></div></div>

<p>Avoid adding TODOs that refer to an individual or team as the context:</p>

<div class="badcode"></div>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">// TODO: username - File an issue and use a '*' for repetition.</span>
</code></pre></div></div>

<p>If your <code class="language-plaintext highlighter-rouge">TODO</code> is of the form “At a future date do something” make sure that you
either include a very specific date (“Fix by November 2005”) or a very specific
event (“Remove this code when all clients can handle XML responses.”).</p>

<p><a id="modifiers"></a></p>

<p><a id="s4.8.7-modifiers"></a></p>

<h4 id="487-modifiers">4.8.7 Modifiers</h4>

<p>Class and member modifiers, when present, appear in the order recommended by the
Java Language Specification:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kd">public</span> <span class="kd">protected</span> <span class="kd">private</span> <span class="kd">abstract</span> <span class="k">default</span> <span class="kd">static</span> <span class="kd">final</span> <span class="n">sealed</span> <span class="n">non</span><span class="o">-</span><span class="n">sealed</span>
  <span class="kd">transient</span> <span class="kd">volatile</span> <span class="kd">synchronized</span> <span class="kd">native</span> <span class="kd">strictfp</span>
</code></pre></div></div>

<p>Modifiers on <code class="language-plaintext highlighter-rouge">requires</code> module directives, when present, appear in the following
order:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">transitive</span> <span class="kd">static</span>
</code></pre></div></div>

<p><a id="s4.8.8-numeric-literals"></a></p>

<h4 id="488-numeric-literals">4.8.8 Numeric Literals</h4>

<p><code class="language-plaintext highlighter-rouge">long</code>-valued integer literals use an uppercase <code class="language-plaintext highlighter-rouge">L</code> suffix, never lowercase (to
avoid confusion with the digit <code class="language-plaintext highlighter-rouge">1</code>). For example, <code class="language-plaintext highlighter-rouge">3000000000L</code> rather than
<code class="language-plaintext highlighter-rouge">3000000000l</code>.</p>

<p><a id="s4.8.9-text-blocks"></a></p>

<h4 id="489-text-blocks">4.8.9 Text Blocks</h4>

<p>The opening <code class="language-plaintext highlighter-rouge">"""</code> of a text block is always on a new line. That line may either
follow the same indentation rules as other constructs, or it may have no
indentation at all (so it starts at the left margin). The closing <code class="language-plaintext highlighter-rouge">"""</code> is on a
new line with the same indentation as the opening <code class="language-plaintext highlighter-rouge">"""</code>, and may be followed on
the same line by further code. Each line of text in the text block is indented
at least as much as the opening and closing <code class="language-plaintext highlighter-rouge">"""</code>. (If a line is indented
further, then the string literal defined by the text block will have space at
the start of that line.)</p>

<p>The contents of a text block may exceed the <a href="#columnlimit">column limit</a>.</p>

<p><a id="naming"></a></p>

<p><a id="s5-naming"></a></p>

<h2 id="5-naming">5 Naming</h2>

<p><a id="s5.1-identifier-names"></a></p>

<h3 id="51-rules-common-to-all-identifiers">5.1 Rules common to all identifiers</h3>

<p>Identifiers use only ASCII letters and digits, and, in a small number of cases
noted below, underscores. Thus each valid identifier name is matched by the
regular expression <code class="language-plaintext highlighter-rouge">\w+</code> .</p>

<p>In Google Style, special prefixes or suffixes are <strong>not</strong> used. For example,
these names are not Google Style: <code class="language-plaintext highlighter-rouge">name_</code>, <code class="language-plaintext highlighter-rouge">mName</code>, <code class="language-plaintext highlighter-rouge">s_name</code> and <code class="language-plaintext highlighter-rouge">kName</code>.</p>

<p><a id="s5.2-specific-identifier-names"></a></p>

<h3 id="52-rules-by-identifier-type">5.2 Rules by identifier type</h3>

<p><a id="s5.2.1-package-names"></a></p>

<h4 id="521-package-and-module-names">5.2.1 Package and module names</h4>

<p>Package and module names use only lowercase letters and digits (no underscores).
Consecutive words are simply concatenated together. For example,
<code class="language-plaintext highlighter-rouge">com.example.deepspace</code>, not <code class="language-plaintext highlighter-rouge">com.example.deepSpace</code> or
<code class="language-plaintext highlighter-rouge">com.example.deep_space</code>.</p>

<p><a id="s5.2.2-class-names"></a></p>

<h4 id="522-class-names">5.2.2 Class names</h4>

<p>Class names are written in <a href="#s5.3-camel-case">UpperCamelCase</a>.</p>

<p>Class names are typically nouns or noun phrases. For example, <code class="language-plaintext highlighter-rouge">Character</code> or
<code class="language-plaintext highlighter-rouge">ImmutableList</code>. Interface names may also be nouns or noun phrases (for example,
<code class="language-plaintext highlighter-rouge">List</code>), but may sometimes be adjectives or adjective phrases instead (for
example, <code class="language-plaintext highlighter-rouge">Readable</code>).</p>

<p>There are no specific rules or even well-established conventions for naming
annotation types.</p>

<p>A <em>test</em> class has a name that ends with <code class="language-plaintext highlighter-rouge">Test</code>, for example,
<code class="language-plaintext highlighter-rouge">HashIntegrationTest</code>. If it covers a single class, its name is the name of that
class plus <code class="language-plaintext highlighter-rouge">Test</code>, for example <code class="language-plaintext highlighter-rouge">HashImplTest</code>.</p>

<p><a id="s5.2.3-method-names"></a></p>

<h4 id="523-method-names">5.2.3 Method names</h4>

<p>Method names are written in <a href="#s5.3-camel-case">lowerCamelCase</a>.</p>

<p>Method names are typically verbs or verb phrases. For example, <code class="language-plaintext highlighter-rouge">sendMessage</code> or
<code class="language-plaintext highlighter-rouge">stop</code>.</p>

<p>Underscores may appear in JUnit <em>test</em> method names to separate logical
components of the name, with <em>each</em> component written in
<a href="#s5.3-camel-case">lowerCamelCase</a>, for example
<code class="language-plaintext highlighter-rouge">transferMoney_deductsFromSource</code>. There is no One Correct Way to name test
methods.</p>

<p><a id="constants"></a></p>

<p><a id="s5.2.4-constant-names"></a></p>

<h4 id="524-constant-names">5.2.4 Constant names</h4>

<p>Constant names use <code class="language-plaintext highlighter-rouge">UPPER_SNAKE_CASE</code>: all uppercase letters, with each word
separated from the next by a single underscore. But what <em>is</em> a constant,
exactly?</p>

<p>Constants are static final fields whose contents are deeply immutable and whose
methods have no detectable side effects. Examples include primitives, strings,
immutable value classes, and anything set to <code class="language-plaintext highlighter-rouge">null</code>. If any of the instance’s
observable state can change, it is not a constant. Merely <em>intending</em> to never
mutate the object is not enough. Examples:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">// Constants</span>
<span class="kd">static</span> <span class="kd">final</span> <span class="kt">int</span> <span class="no">NUMBER</span> <span class="o">=</span> <span class="mi">5</span><span class="o">;</span>
<span class="kd">static</span> <span class="kd">final</span> <span class="nc">ImmutableList</span><span class="o">&lt;</span><span class="nc">String</span><span class="o">&gt;</span> <span class="no">NAMES</span> <span class="o">=</span> <span class="nc">ImmutableList</span><span class="o">.</span><span class="na">of</span><span class="o">(</span><span class="s">"Ed"</span><span class="o">,</span> <span class="s">"Ann"</span><span class="o">);</span>
<span class="kd">static</span> <span class="kd">final</span> <span class="nc">Map</span><span class="o">&lt;</span><span class="nc">String</span><span class="o">,</span> <span class="nc">Integer</span><span class="o">&gt;</span> <span class="no">AGES</span> <span class="o">=</span> <span class="nc">ImmutableMap</span><span class="o">.</span><span class="na">of</span><span class="o">(</span><span class="s">"Ed"</span><span class="o">,</span> <span class="mi">35</span><span class="o">,</span> <span class="s">"Ann"</span><span class="o">,</span> <span class="mi">32</span><span class="o">);</span>
<span class="kd">static</span> <span class="kd">final</span> <span class="nc">Joiner</span> <span class="no">COMMA_JOINER</span> <span class="o">=</span> <span class="nc">Joiner</span><span class="o">.</span><span class="na">on</span><span class="o">(</span><span class="sc">','</span><span class="o">);</span> <span class="c1">// because Joiner is immutable</span>
<span class="kd">static</span> <span class="kd">final</span> <span class="nc">SomeMutableType</span><span class="o">[]</span> <span class="no">EMPTY_ARRAY</span> <span class="o">=</span> <span class="o">{};</span>

<span class="c1">// Not constants</span>
<span class="kd">static</span> <span class="nc">String</span> <span class="n">nonFinal</span> <span class="o">=</span> <span class="s">"non-final"</span><span class="o">;</span>
<span class="kd">final</span> <span class="nc">String</span> <span class="n">nonStatic</span> <span class="o">=</span> <span class="s">"non-static"</span><span class="o">;</span>
<span class="kd">static</span> <span class="kd">final</span> <span class="nc">Set</span><span class="o">&lt;</span><span class="nc">String</span><span class="o">&gt;</span> <span class="n">mutableCollection</span> <span class="o">=</span> <span class="k">new</span> <span class="nc">HashSet</span><span class="o">&lt;</span><span class="nc">String</span><span class="o">&gt;();</span>
<span class="kd">static</span> <span class="kd">final</span> <span class="nc">ImmutableSet</span><span class="o">&lt;</span><span class="nc">SomeMutableType</span><span class="o">&gt;</span> <span class="n">mutableElements</span> <span class="o">=</span> <span class="nc">ImmutableSet</span><span class="o">.</span><span class="na">of</span><span class="o">(</span><span class="n">mutable</span><span class="o">);</span>
<span class="kd">static</span> <span class="kd">final</span> <span class="nc">ImmutableMap</span><span class="o">&lt;</span><span class="nc">String</span><span class="o">,</span> <span class="nc">SomeMutableType</span><span class="o">&gt;</span> <span class="n">mutableValues</span> <span class="o">=</span>
    <span class="nc">ImmutableMap</span><span class="o">.</span><span class="na">of</span><span class="o">(</span><span class="s">"Ed"</span><span class="o">,</span> <span class="n">mutableInstance</span><span class="o">,</span> <span class="s">"Ann"</span><span class="o">,</span> <span class="n">mutableInstance2</span><span class="o">);</span>
<span class="kd">static</span> <span class="kd">final</span> <span class="nc">Logger</span> <span class="n">logger</span> <span class="o">=</span> <span class="nc">Logger</span><span class="o">.</span><span class="na">getLogger</span><span class="o">(</span><span class="nc">MyClass</span><span class="o">.</span><span class="na">getName</span><span class="o">());</span>
<span class="kd">static</span> <span class="kd">final</span> <span class="nc">String</span><span class="o">[]</span> <span class="n">nonEmptyArray</span> <span class="o">=</span> <span class="o">{</span><span class="s">"these"</span><span class="o">,</span> <span class="s">"can"</span><span class="o">,</span> <span class="s">"change"</span><span class="o">};</span>
</code></pre></div></div>

<p>These names are typically nouns or noun phrases.</p>

<p><a id="s5.2.5-non-constant-field-names"></a></p>

<h4 id="525-non-constant-field-names">5.2.5 Non-constant field names</h4>

<p>Non-constant field names (static or otherwise) are written in
<a href="#s5.3-camel-case">lowerCamelCase</a>.</p>

<p>These names are typically nouns or noun phrases. For example, <code class="language-plaintext highlighter-rouge">computedValues</code>
or <code class="language-plaintext highlighter-rouge">index</code>.</p>

<p><a id="s5.2.6-parameter-names"></a></p>

<h4 id="526-parameter-names">5.2.6 Parameter names</h4>

<p>Parameter names are written in <a href="#s5.3-camel-case">lowerCamelCase</a>.</p>

<p>One-character parameter names in public methods should be avoided.</p>

<p><a id="s5.2.7-local-variable-names"></a></p>

<h4 id="527-local-variable-names">5.2.7 Local variable names</h4>

<p>Local variable names are written in <a href="#s5.3-camel-case">lowerCamelCase</a>.</p>

<p>Even when final and immutable, local variables are not considered to be
constants, and should not be styled as constants.</p>

<p><a id="s5.2.8-type-variable-names"></a></p>

<h4 id="528-type-variable-names">5.2.8 Type variable names</h4>

<p>Each type variable is named in one of two styles:</p>

<ul>
  <li>A single capital letter, optionally followed by a single numeral (such as
<code class="language-plaintext highlighter-rouge">E</code>, <code class="language-plaintext highlighter-rouge">T</code>, <code class="language-plaintext highlighter-rouge">X</code>, <code class="language-plaintext highlighter-rouge">T2</code>)</li>
  <li>A name in the form used for classes (see Section 5.2.2,
<a href="#s5.2.2-class-names">Class names</a>), followed by the capital letter <code class="language-plaintext highlighter-rouge">T</code>
(examples: <code class="language-plaintext highlighter-rouge">RequestT</code>, <code class="language-plaintext highlighter-rouge">FooBarT</code>).</li>
</ul>

<p><a id="s5.2.9-unnamed-variables"></a></p>

<h4 id="529-unnamed-variables">5.2.9 Unnamed variables</h4>

<p>The <code class="language-plaintext highlighter-rouge">_</code> syntax for unnamed variables and parameters is allowed wherever it is
applicable. For example:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nc">Predicate</span><span class="o">&lt;</span><span class="nc">String</span><span class="o">&gt;</span> <span class="n">alwaysTrue</span> <span class="o">=</span> <span class="n">_</span> <span class="o">-&gt;</span> <span class="kc">true</span><span class="o">;</span>
</code></pre></div></div>

<p><a id="acronyms"></a></p>

<p><a id="camelcase"></a></p>

<p><a id="s5.3-camel-case"></a></p>

<h3 id="53-camel-case-defined">5.3 Camel case: defined</h3>

<p>Sometimes there is more than one reasonable way to convert an English phrase
into camel case, such as when acronyms or unusual constructs like “IPv6” or
“iOS” are present. To improve predictability, Google Style specifies the
following (nearly) deterministic scheme.</p>

<p>Beginning with the prose form of the name:</p>

<ol>
  <li>
    <p>Convert the phrase to plain ASCII and remove any apostrophes. For example,
“Müller’s algorithm” might become “Muellers algorithm”.</p>
  </li>
  <li>
    <p>Divide this result into words, splitting on spaces and any remaining
punctuation (typically hyphens).</p>

    <ul>
      <li><em>Recommended:</em> if any word already has a conventional camel-case
appearance in common usage, split this into its constituent parts (e.g.,
“AdWords” becomes “ad words”). Note that a word such as “iOS” is not
really in camel case <em>per se</em>; it defies <em>any</em> convention, so this
recommendation does not apply.</li>
    </ul>
  </li>
  <li>
    <p>Now lowercase <em>everything</em> (including acronyms), then uppercase only the
first character of:</p>

    <ul>
      <li>… each word, to yield <em>upper camel case</em>, or</li>
      <li>… each word except the first, to yield <em>lower camel case</em></li>
    </ul>
  </li>
  <li>
    <p>Finally, join all the words into a single identifier. Note that the casing
of the original words is almost entirely disregarded.</p>
  </li>
</ol>

<p>In very rare circumstances (for example, multipart version numbers), you may
need to use underscores to separate adjacent numbers, since numbers do not have
upper and lower case variants.</p>

<p>Examples:</p>

<!-- mdformat off -->

<table>
  <thead>
    <tr>
      <th style="text-align: left">Prose form</th>
      <th style="text-align: left">Correct</th>
      <th style="text-align: left">Incorrect</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left">“XML HTTP request”</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">XmlHttpRequest</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">XMLHTTPRequest</code></td>
    </tr>
    <tr>
      <td style="text-align: left">“new customer ID”</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">newCustomerId</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">newCustomerID</code></td>
    </tr>
    <tr>
      <td style="text-align: left">“inner stopwatch”</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">innerStopwatch</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">innerStopWatch</code></td>
    </tr>
    <tr>
      <td style="text-align: left">“supports IPv6 on iOS?”</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">supportsIpv6OnIos</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">supportsIPv6OnIOS</code></td>
    </tr>
    <tr>
      <td style="text-align: left">“YouTube importer”</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">YouTubeImporter</code><br /><code class="language-plaintext highlighter-rouge">YoutubeImporter</code>*</td>
      <td style="text-align: left"> </td>
    </tr>
    <tr>
      <td style="text-align: left">“Turn on 2SV”</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">turnOn2sv</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">turnOn2Sv</code></td>
    </tr>
    <tr>
      <td style="text-align: left">“Guava 33.4.6”</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">guava33_4_6</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">guava3346</code></td>
    </tr>
  </tbody>
</table>

<!-- mdformat on -->

<p>*Acceptable, but not recommended.</p>

<p><strong>Note:</strong> Some words are ambiguously hyphenated in the English language: for
example “nonempty” and “non-empty” are both correct, so the method names
<code class="language-plaintext highlighter-rouge">checkNonempty</code> and <code class="language-plaintext highlighter-rouge">checkNonEmpty</code> are likewise both correct.</p>

<p><a id="s6-programming-practices"></a></p>

<h2 id="6-programming-practices">6 Programming Practices</h2>

<p><a id="s6.1-override-annotation"></a></p>

<h3 id="61-override-always-used">6.1 <code class="language-plaintext highlighter-rouge">@Override</code>: always used</h3>

<p>A method is marked with the <code class="language-plaintext highlighter-rouge">@Override</code> annotation whenever it is legal. This
includes a class method overriding a superclass method, a class method
implementing an interface method, an interface method respecifying a
superinterface method, and an explicitly declared accessor method for a record
component.</p>

<p><strong>Exception:</strong> <code class="language-plaintext highlighter-rouge">@Override</code> may be omitted when the parent method is
<code class="language-plaintext highlighter-rouge">@Deprecated</code>.</p>

<p><a id="caughtexceptions"></a></p>

<p><a id="s6.2-caught-exceptions"></a></p>

<h3 id="62-caught-exceptions-not-ignored">6.2 Caught exceptions: not ignored</h3>

<p>It is very rarely correct to do nothing in response to a caught exception.
(Typical responses are to log it, or if it is considered “impossible”, rethrow
it as an <code class="language-plaintext highlighter-rouge">AssertionError</code>.)</p>

<p>When it truly is appropriate to take no action whatsoever in a catch block, the
reason this is justified is explained in a comment.</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">try</span> <span class="o">{</span>
  <span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="nc">Integer</span><span class="o">.</span><span class="na">parseInt</span><span class="o">(</span><span class="n">response</span><span class="o">);</span>
  <span class="k">return</span> <span class="nf">handleNumericResponse</span><span class="o">(</span><span class="n">i</span><span class="o">);</span>
<span class="o">}</span> <span class="k">catch</span> <span class="o">(</span><span class="nc">NumberFormatException</span> <span class="n">_</span><span class="o">)</span> <span class="o">{</span>
  <span class="c1">// it's not numeric; that's fine, just continue</span>
<span class="o">}</span>
<span class="k">return</span> <span class="nf">handleTextResponse</span><span class="o">(</span><span class="n">response</span><span class="o">);</span>
</code></pre></div></div>

<p><a id="s6.3-static-members"></a></p>

<h3 id="63-static-members-qualified-using-class">6.3 Static members: qualified using class</h3>

<p>When a reference to a static class member must be qualified, it is qualified
with that class’s name, not with a reference or expression of that class’s type.</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nc">Foo</span> <span class="n">aFoo</span> <span class="o">=</span> <span class="o">...;</span>
<span class="nc">Foo</span><span class="o">.</span><span class="na">aStaticMethod</span><span class="o">();</span> <span class="c1">// good</span>
<span class="n">aFoo</span><span class="o">.</span><span class="na">aStaticMethod</span><span class="o">();</span> <span class="c1">// bad</span>
<span class="n">somethingThatYieldsAFoo</span><span class="o">().</span><span class="na">aStaticMethod</span><span class="o">();</span> <span class="c1">// very bad</span>
</code></pre></div></div>

<p><a id="finalizers"></a></p>

<p><a id="s6.4-finalizers"></a></p>

<h3 id="64-finalizers-not-used">6.4 Finalizers: not used</h3>

<p>Do not override <code class="language-plaintext highlighter-rouge">Object.finalize</code>. Finalization support is
<a href="https://openjdk.org/jeps/421"><em>scheduled for removal</em></a>.</p>

<p><a id="javadoc"></a></p>

<p><a id="s7-javadoc"></a></p>

<h2 id="7-javadoc">7 Javadoc</h2>

<p><a id="s7.1-javadoc-formatting"></a></p>

<h3 id="71-formatting">7.1 Formatting</h3>

<p><a id="s7.1.1-javadoc-multi-line"></a></p>

<h4 id="711-general-form">7.1.1 General form</h4>

<p>Both Markdown Javadoc and Traditional Javadoc are acceptable. Markdown Javadoc
looks like this example:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">/// Javadoc text is written here,</span>
<span class="c1">/// wrapped normally...</span>
<span class="kd">public</span> <span class="kt">int</span> <span class="nf">method</span><span class="o">(</span><span class="nc">String</span> <span class="n">p1</span><span class="o">)</span> <span class="o">{</span> <span class="o">...</span> <span class="o">}</span>
</code></pre></div></div>

<p>The <em>basic</em> formatting of Traditional Javadoc blocks is as seen in this example:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cm">/**
 * Multiple lines of Javadoc text are written here,
 * wrapped normally...
 */</span>
<span class="kd">public</span> <span class="kt">int</span> <span class="nf">method</span><span class="o">(</span><span class="nc">String</span> <span class="n">p1</span><span class="o">)</span> <span class="o">{</span> <span class="o">...</span> <span class="o">}</span>
</code></pre></div></div>

<p>… or in this single-line example:</p>

<div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cm">/** An especially short bit of Javadoc. */</span>
</code></pre></div></div>

<p>The basic form is always acceptable. The single-line form may be substituted
when the entirety of the Javadoc block (including comment markers) can fit on a
single line. Note that this only applies when there are no block tags such as
<code class="language-plaintext highlighter-rouge">@param</code>.</p>

<p><a id="s7.1.2-javadoc-paragraphs"></a></p>

<h4 id="712-paragraphs">7.1.2 Paragraphs</h4>

<p>With Traditional Javadoc, one blank line—that is, a line containing only the
aligned leading asterisk (<code class="language-plaintext highlighter-rouge">*</code>)—appears between paragraphs, and before the group
of block tags if present. Each paragraph except the first has <code class="language-plaintext highlighter-rouge">&lt;p&gt;</code> immediately
before the first word, with no space after it. HTML tags for other block-level
elements, such as <code class="language-plaintext highlighter-rouge">&lt;ul&gt;</code> or <code class="language-plaintext highlighter-rouge">&lt;table&gt;</code>, are <em>not</em> preceded with <code class="language-plaintext highlighter-rouge">&lt;p&gt;</code>.</p>

<p>With Markdown Javadoc, paragraphs are separated as usual for Markdown, by a line
that is blank apart from the leading <code class="language-plaintext highlighter-rouge">///</code>. No <code class="language-plaintext highlighter-rouge">&lt;p&gt;</code> is needed.</p>

<p><a id="s7.1.3-javadoc-at-clauses"></a> <!-- historical link --></p>

<p><a id="s7.1.3-javadoc-block-tags"></a></p>

<h4 id="713-block-tags">7.1.3 Block tags</h4>

<p>Any of the standard “block tags” that are used appear in the order <code class="language-plaintext highlighter-rouge">@param</code>,
<code class="language-plaintext highlighter-rouge">@return</code>, <code class="language-plaintext highlighter-rouge">@throws</code>, <code class="language-plaintext highlighter-rouge">@deprecated</code>, and these four types never appear with an
empty description. When a block tag doesn’t fit on a single line, continuation
lines are indented four (or more) spaces from the position of the <code class="language-plaintext highlighter-rouge">@</code> for
Traditional Javadoc, and exactly two spaces for Markdown Javadoc. (A four-space
indentation in Markdown is interpreted as an indented code block in some
contexts.)</p>

<p><a id="s7.2-summary-fragment"></a></p>

<h3 id="72-the-summary-fragment">7.2 The summary fragment</h3>

<p>Each Javadoc block begins with a brief <strong>summary fragment</strong>. This fragment is
very important: it is the only part of the text that appears in certain contexts
such as class and method indexes.</p>

<p>This is a fragment—a noun phrase or verb phrase, not a complete sentence. It
does <strong>not</strong> begin with <code class="language-plaintext highlighter-rouge">A `Foo` is a...</code>, or <code class="language-plaintext highlighter-rouge">This method returns...</code>, nor
does it form a complete imperative sentence like <code class="language-plaintext highlighter-rouge">Save the record.</code>. However,
the fragment is capitalized and punctuated as if it were a complete sentence.</p>

<p><strong>Tip:</strong> A common mistake is to write simple Javadoc in the form
<code class="language-plaintext highlighter-rouge">/// @return the customer ID</code>. This is incorrect, and should be changed to
<code class="language-plaintext highlighter-rouge">/// Returns the customer ID.</code> or <code class="language-plaintext highlighter-rouge">/// {@return the customer ID}</code>.</p>

<p><a id="s7.3.3-javadoc-optional"></a> <!-- historical link --></p>

<p><a id="s7.3-javadoc-where-required"></a></p>

<h3 id="73-where-javadoc-is-used">7.3 Where Javadoc is used</h3>

<p>At the <em>minimum</em>, Javadoc is present for every <em>visible</em> class, member, or
record component, with a few exceptions noted below. A top-level class is
visible if it is <code class="language-plaintext highlighter-rouge">public</code>; a member is visible if it is <code class="language-plaintext highlighter-rouge">public</code> or <code class="language-plaintext highlighter-rouge">protected</code>
and its containing class is visible; and a record component is visible if its
containing record is visible.</p>

<p>Additional Javadoc content may also be present, as explained in Section 7.3.4,
<a href="#s7.3.4-javadoc-non-required">Non-required Javadoc</a>.</p>

<p><a id="s7.3.1-javadoc-exception-self-explanatory"></a></p>

<h4 id="731-exception-self-explanatory-members">7.3.1 Exception: self-explanatory members</h4>

<p>Javadoc is optional for “simple, obvious” members and record components, such as
a <code class="language-plaintext highlighter-rouge">getFoo()</code> method, <em>if</em> there <em>really and truly</em> is nothing else worthwhile to
say but “the foo”.</p>

<p><strong>Important:</strong> it is not appropriate to cite this exception to justify omitting
relevant information that a typical reader might need to know. For example, for
a record component named <code class="language-plaintext highlighter-rouge">canonicalName</code>, don’t omit its documentation (with the
rationale that it would say only <code class="language-plaintext highlighter-rouge">@param canonicalName the canonical name</code>) if a
typical reader may have no idea what the term “canonical name” means!</p>

<p><a id="s7.3.2-javadoc-exception-overrides"></a></p>

<h4 id="732-exception-overrides">7.3.2 Exception: overrides</h4>

<p>Javadoc is not always present on a method that overrides a supertype method.</p>

<p><a id="s7.3.4-javadoc-non-required"></a></p>

<h4 id="734-non-required-javadoc">7.3.4 Non-required Javadoc</h4>

<p>Other classes, members, and record components have Javadoc <em>as needed or
desired</em>.</p>

<p>Whenever an implementation comment would be used to define the overall purpose
or behavior of a class or member, that comment is written as Javadoc instead
(using <code class="language-plaintext highlighter-rouge">///</code> or <code class="language-plaintext highlighter-rouge">/**</code>).</p>

<p>Non-required Javadoc is not strictly required to follow the formatting rules of
Sections 7.1.1, 7.1.2, 7.1.3, and 7.2, though it is of course recommended.</p>

<!-- NB: Keep this at the end of the file. See comment at top for details.
      -->


      <div class="footer border-top border-gray-light mt-5 pt-3 text-right text-gray">
        This site is open source. <a href="https://github.com/google/styleguide/edit/gh-pages/javaguide.md">Improve this page</a>.
      </div>

    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/anchor-js/4.1.0/anchor.min.js" integrity="sha256-lZaRhKri35AyJSypXXs4o6OPFTbTmUoltBbDCbdzegg=" crossorigin="anonymous"></script>
    <script>anchors.add();</script>
  </body>
</html>