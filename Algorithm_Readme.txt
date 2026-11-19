\documentclass[11pt,a4paper]{article}
% ==============================================================================
% COMPREHENSIVE LATeX-STRUCTURED PLAIN-TEXT ANALYTICAL COMPANION & MANIFEST
% Author: Yash
% Textbook: Kenneth H. Rosen, Discrete Mathematics and Its Applications, 8th Ed.
% Chapter 3: Algorithms (Sections 3.1, 3.2, and 3.3, pp. 201--249)
% ==============================================================================

\title{Algorithms in Five Case Studies: Theory, Proofs, and Empirical Analysis}
\author{Yash}
\date{November 19, 2026}
\course{Discrete Mathematics (Rosen, 8th Edition, Chapter 3)}

\begin{document}

% ==============================================================================
% SECTION 1: SUBMISSION ARCHIVE MANIFEST & EXECUTION GUIDE
% ==============================================================================
\section{Submission Package Manifest (4-File Archive)}

This submission archive contains four synchronized, self-contained artifacts
designed to satisfy every core and optional requirement of the Chapter 3
Algorithms assignment:

\begin{enumerate}
  \item \textbf{rosen\_ch3\_analytical\_note.pdf} (Compiled from \texttt{rosen\_ch3\_analytical\_note.tex}):
        The primary academic analytical note formatted in LaTeX. It covers:
        \begin{itemize}
          \item Formal definition of an algorithm and the algorithm-vs-program distinction.
          \item Verification of Rosen's seven algorithmic properties and formal loop-invariant/termination proofs.
          \item Taxonomy of algorithmic paradigms (Brute Force, Decrease-and-Conquer, Divide-and-Conquer, Greedy, and Prefix-Jump Precomputation).
          \item Asymptotic growth theory ($\text{Big-}O$, $\text{Big-}\Omega$, $\text{Big-}\Theta$), witness proofs, combination theorems, and logarithmic PGFPlots graphs.
          \item Worst-case, average-case, and best-case complexity derivations, physical wall-clock runtime tables, Tractability ($\text{P}$ vs.\ $\text{NP}$, Cook--Levin Theorem), and Turing's Halting Problem.
          \item Empirical operation tables, benchmark plots, and complete Appendix A source listings.
        \end{itemize}

  \item \textbf{rosen\_ch3\_algos.py}:
        Standalone, zero-dependency Python 3 implementation and benchmark suite.
        Every algorithm is instrumented to return both its computed result and
        its exact primitive operation count (element comparisons, character checks,
        arithmetic operations, or subset checks) rather than machine-dependent
        wall-clock seconds.
        \begin{itemize}
          \item \emph{Execution Command:} \texttt{python3 rosen\_ch3\_algos.py}
        \end{itemize}

  \item \textbf{rosen\_ch3\_dashboard.html}:
        Responsive, self-contained interactive web dashboard (no external CDN
        or server dependencies). Features:
        \begin{itemize}
          \item Manual \textbf{Light Mode / Dark Mode} theme toggle and responsive mobile/desktop grid layout.
          \item Global \textbf{Simulated Processor Speed} selector ($10^6$, $10^9$, and $10^{11}$ ops/sec).
          \item Interactive \textbf{Big-$O$ Witness Verifier} testing $f(n) = 4n^2 + 6n\log_2 n + 10 \le C \cdot g(n)$ across $1 \le n \le 100{,}000$.
          \item Five interactive case-study modules with live input-size sliders, KPI speedup cards, dual logarithmic SVG plots (operations and physical runtime), and hover tooltips showing formal proofs and Python source code.
          \item Three live step-by-step algorithm sandboxes: Binary Search interval halving tracer, Naive String Matcher shift analyzer, and Greedy Talk Scheduler Gantt timeline visualizer.
        \end{itemize}

  \item \textbf{README.txt} (This File):
        A LaTeX-structured plain-text reference companion summarizing all definitions,
        theorems, formal proofs, complexity derivations, and verified console outputs.
\end{enumerate}

% ==============================================================================
% SECTION 2: WHAT IS AN ALGORITHM? (ROSEN SECTION 3.1)
% ==============================================================================
\section{What Is an Algorithm? (Rosen \S3.1)}

\begin{definition}[Algorithm --- Rosen \S3.1, Definition 1]
An \emph{algorithm} is a finite sequence of precise instructions for performing
a computation or for solving a problem.
\end{definition}

\subsection{Algorithm vs.\ Computer Program}
An algorithm is an abstract, hardware- and language-independent mathematical
procedure (typically expressed in structured English or pseudocode), whereas
a computer program is a concrete implementation written in a specific programming
language (e.g., Python, C++, Java). A single computational problem can be solved
by many distinct algorithms whose operation counts differ by orders of magnitude.

\subsection{Rosen's Seven Properties of Algorithms}
Every valid algorithm must satisfy seven foundational properties (\S3.1.1):
\begin{enumerate}
  \item \textbf{Input:} Has input values drawn from a specified set.
  \item \textbf{Output:} Produces output values from a specified set representing the solution.
  \item \textbf{Definiteness:} Every step is defined precisely and unambiguously.
  \item \textbf{Correctness:} Produces the exact right output for every valid input instance.
  \item \textbf{Finiteness:} Terminates after a finite number of steps for every input.
  \item \textbf{Effectiveness:} Every step can be performed exactly in a finite amount of time.
  \item \textbf{Generality:} Applies to all problems of the desired form, not just isolated inputs.
\end{enumerate}

\subsection{Formal Loop-Invariant and Termination Proof (Binary Search)}
\begin{theorem}[Correctness and Termination of Binary Search --- Rosen Algorithm 3]
Given a strictly increasing sequence $a_1 < a_2 < \dots < a_n$ ($n \ge 1$) and a
target integer $x$, Binary Search terminates in at most $\lceil \log_2 n \rceil$
loop iterations and returns $k$ if $x = a_k$, or $0$ if $x$ is absent.
\end{theorem}

\begin{proof}
\textbf{Loop Invariant:} At the start of each iteration of \texttt{while} $i < j$,
$x \in \{a_1, \dots, a_n\} \iff x \in \{a_i, \dots, a_j\}$.
\begin{itemize}
  \item \emph{Initialization:} Initially $i = 1$ and $j = n$, so $\{a_i, \dots, a_j\}$ equals the full list.
  \item \emph{Maintenance:} Assume $i < j$ and let $m = \lfloor (i + j)/2 \rfloor$, which guarantees $i \le m < j$. Since $a_1 < \dots < a_n$:
        \begin{itemize}
          \item If $x > a_m$, then $x > a_r$ for all $r \le m$, so $x \notin \{a_i, \dots, a_m\}$. Setting $i := m + 1$ preserves the invariant.
          \item If $x \le a_m$, then $x < a_r$ for all $r > m$, so $x \notin \{a_{m+1}, \dots, a_j\}$. Setting $j := m$ preserves the invariant.
        \end{itemize}
  \item \emph{Termination:} Define the interval length $L = j - i + 1 \ge 2$. In both branches, the new length $L'$ satisfies $L' \le \lceil L/2 \rceil < L$. Because $L$ is a strictly decreasing positive integer, the loop must terminate at $L = 1$ ($i = j$). By the invariant, $x$ is in the list iff $x = a_i$.
\end{itemize}
\end{proof}

% ==============================================================================
% SECTION 3: ALGORITHMIC PARADIGMS ACROSS FIVE CASE STUDIES
% ==============================================================================
\section{Types of Algorithms and Algorithmic Paradigms}

\begin{table}[h!]
\caption{Taxonomy of Paradigms and Complexity Across the Five Case Studies}
\begin{tabular}{llll}
\hline
Case Study & Paradigm Shift & Slow Method & Fast Method \\
\hline
1. Ordered Searching & Brute Force $\to$ Decrease-and-Conquer & Linear: $\Theta(n)$ & Binary: $\Theta(\log_2 n)$ \\
2. List Sorting & Quadratic $\to$ Divide-and-Conquer & Bubble/Ins: $\Theta(n^2)$ & Merge Sort: $\Theta(n\log_2 n)$ \\
3. String Matching & Sliding Window $\to$ Prefix Reuse & Naive: $\Theta(nm)$ & KMP: $\Theta(n + m)$ \\
4. Polynomial Eval & Power Loop $\to$ Algebraic Nesting & Conv: $3n = \Theta(n)$ & Horner: $2n = \Theta(n)$ \\
5. Talk Scheduling & Exhaustive Subsets $\to$ Greedy EFT & Subsets: $\Theta(n 2^n)$ & Greedy: $\Theta(n\log_2 n)$ \\
\hline
\end{tabular}
\end{table}

\subsection{Detailed Paradigm Notes}
\begin{itemize}
  \item \textbf{Case Study 1 (Searching):} Linear Search (\S3.1.2, Alg.\ 2) inspects items sequentially ($2n + 2$ comparisons when absent). Binary Search (\S3.1.2, Alg.\ 3) exploits total ordering to halve the interval each pass ($2\lfloor \log_2 n \rfloor + 2$ comparisons).
  \item \textbf{Case Study 2 (Sorting):} Bubble Sort (\S3.1.3, Alg.\ 4) always performs $\frac{n(n-1)}{2}$ adjacent comparisons. Insertion Sort (\S3.1.3, Alg.\ 5) takes $n - 1$ comparisons on sorted inputs (best case) but $\frac{n(n+1)}{2} - 1$ on reverse-sorted inputs (worst case). Divide-and-conquer Merge Sort (\S3.3.2 / \S5.4) guarantees $O(n\log_2 n)$ comparisons on all inputs.
  \item \textbf{Case Study 3 (String Matching):} Naive String Matching (\S3.1.4, Alg.\ 6) tests all $n - m + 1$ shifts, degrading to $(n - m + 1)m$ character checks on adversarial repetitive strings ($T = \texttt{a}^{n-1}\texttt{b}$, $P = \texttt{a}^{m-1}\texttt{b}$). The KMP algorithm precomputes a longest-proper-prefix-suffix (\texttt{lps}) array in $\Theta(m)$ time so text indices never backtrack, achieving $\Theta(n + m)$ comparisons.
  \item \textbf{Case Study 4 (Polynomial Evaluation):} Evaluating $P(c) = \sum_{i=0}^{n} a_i c^i$ (\S3.3, Ex.\ 13--14) conventionally uses $2n$ multiplications and $n$ additions ($3n$ arithmetic ops). Horner's nested factoring $P(c) = (\dots((a_n c + a_{n-1})c + \dots)c + a_0)$ uses exactly $n$ multiplications and $n$ additions ($2n$ ops), cutting multiplications by $50\%$.
  \item \textbf{Case Study 5 (Greedy Optimization):} In lecture-hall talk scheduling (\S3.1.5, Alg.\ 8), sorting by \emph{earliest start time} or \emph{shortest duration} fails on counterexample intervals, whereas sorting by \textbf{earliest finish time} ($e_1 \le e_2 \le \dots \le e_n$) is provably optimal via an exchange argument, reducing $\Theta(n 2^n)$ subset enumeration to $\Theta(n\log_2 n)$.
\end{itemize}

% ==============================================================================
% SECTION 4: GROWTH OF FUNCTIONS & COMPLEXITY THEORY (ROSEN SECTIONS 3.2--3.3)
% ==============================================================================
\section{The Growth of Functions and Complexity Theory}

\begin{definition}[Asymptotic Bounds --- Rosen \S3.2]
Let $f$ and $g$ be functions from $\mathbb{Z}$ or $\mathbb{R}$ to $\mathbb{R}$:
\begin{itemize}
  \item $f(x) = O(g(x))$ iff $\exists C, k$ such that $|f(x)| \le C|g(x)|$ whenever $x > k$.
  \item $f(x) = \Omega(g(x))$ iff $\exists C > 0, k$ such that $|f(x)| \ge C|g(x)|$ whenever $x > k$.
  \item $f(x) = \Theta(g(x))$ iff $f(x) = O(g(x))$ and $f(x) = \Omega(g(x))$.
\end{itemize}
\end{definition}

\begin{theorem}[Worked Witness Proof]
Let $f(n) = 4n^2 + 6n\log_2 n + 10$. Then $f(n) = \Theta(n^2)$.
\end{theorem}
\begin{proof}
For all $n \ge 1$, $0 \le \log_2 n < n$ and $1 \le n^2$. Hence:
\[
  4n^2 \le 4n^2 + 6n\log_2 n + 10 \le 4n^2 + 6n^2 + 10n^2 = 20n^2 \quad \forall n > 1.
\]
Thus $C_1 = 4$, $C_2 = 20$, and $k = 1$ serve as witnesses proving $f(n) = \Theta(n^2)$.
\end{proof}

\subsection{Asymptotic Hierarchy, Tractability, P vs.\ NP, and Halting Problem}
\begin{itemize}
  \item \textbf{Standard Dominance Hierarchy:}
        $1 \prec \log_2 n \prec \sqrt{n} \prec n \prec n\log_2 n \prec n^2 \prec n^3 \prec 2^n \prec n!$.
  \item \textbf{Tractability (Class P):} Problems solvable by a deterministic algorithm with worst-case polynomial time complexity $O(n^b)$ are \emph{tractable} (Class $\text{P}$). Problems requiring super-polynomial time ($\Omega(2^n)$, $\Omega(n!)$) are \emph{intractable}.
  \item \textbf{Class NP and NP-Completeness:} Class $\text{NP}$ consists of decision problems whose candidate solutions can be \emph{verified} in polynomial time. By the \textbf{Cook--Levin Theorem}, Boolean Satisfiability (\textsc{SAT}) is $\text{NP}$-complete: every problem in $\text{NP}$ reduces to \textsc{SAT} in polynomial time. Whether $\text{P} = \text{NP}$ remains an open Millennium Prize Problem.
  \item \textbf{Unsolvable Problems (Turing's Halting Problem, \S3.1.6):} No general algorithm $H(P, I)$ can determine whether an arbitrary program $P$ halts on input $I$. Assuming $H$ exists and constructing $K(P)$ to do the opposite of $H(P, P)$ yields an inescapable contradiction on $K(K)$.
\end{itemize}

% ==============================================================================
% SECTION 5: VERIFIED EMPIRICAL BENCHMARK LOGS (rosen_ch3_algos.py)
% ==============================================================================
\section{Verified Empirical Benchmark Logs}

\begin{verbatim}
========================================================================
1. ORDERED SEARCHING: Linear Search vs. Binary Search (Worst Case)
========================================================================
       n   Linear (Worst)   Linear (Avg)   Binary (Worst)
      10               22           12.0                8
     100              202          102.0               14
   1,000            2,002        1,002.0               20
  10,000           20,002       10,002.0               28
 100,000          200,002      100,002.0               34

========================================================================
2. COMPARISON SORTING: Bubble vs. Insertion vs. Merge Sort (Reverse Input)
========================================================================
       n         Bubble      Insertion     Merge Sort
      20            190            190             54
      50          1,225          1,225            189
     100          4,950          4,950            476
     250         31,125         31,125          1,496
     500        124,750        124,750          3,492
   1,000        499,500        499,500          7,984

========================================================================
3. EXACT STRING MATCHING: Naive vs. KMP (Adversarial T='a'^(n-1)+'b')
========================================================================
       n      m     Naive Comps     KMP Comps
     100     50           2,550           198
     250     50          10,050           498
     500     50          22,550           998
   1,000     50          47,550         1,998
   2,500     50         122,550         4,998
   5,000     50         247,550         9,998

========================================================================
4. POLYNOMIAL EVALUATION: Conventional vs. Horner's Rule
========================================================================
Degree   10: Conventional =    30 ops | Horner =    20 ops
Degree  100: Conventional =   300 ops | Horner =   200 ops
Degree 1000: Conventional = 3,000 ops | Horner = 2,000 ops

========================================================================
5. TALK SCHEDULING: Brute-Force Subsets vs. Greedy Earliest-Finish-Time
========================================================================
 n talks    Brute-Force Ops   Greedy EFT Ops
       6                146               16
      10              3,058               33
      14             65,510               52
      18          1,310,692               74
      22         25,165,794               98

========================================================================
6. BIG-THETA WITNESS VERIFICATION: f(n) = 4n^2 + 6n log2(n) + 10
========================================================================
4*n^2 <= f(n) <= 20*n^2 for all 1 <= n <= 100,000: True
f(10^6) / 10^12 = 4.0001
\end{verbatim}

% ==============================================================================
% SECTION 6: ACADEMIC REFERENCES
% ==============================================================================
\begin{thebibliography}{9}
  \bibitem{rosen} K.~H.~Rosen, \emph{Discrete Mathematics and Its Applications}, 8th ed., McGraw-Hill Education, 2019, Chapter~3: Algorithms, pp.~201--249.
  \bibitem{clrs} T.~H.~Cormen, C.~E.~Leiserson, R.~L.~Rivest, and C.~Stein, \emph{Introduction to Algorithms}, 4th ed., MIT Press, 2022.
  \bibitem{knuth} D.~E.~Knuth, \emph{The Art of Computer Programming, Vol.~1 \& Vol.~3}, Addison-Wesley, 1997--1998.
  \bibitem{cook} S.~A.~Cook, ``The Complexity of Theorem-Proving Procedures,'' \emph{Proc.\ 3rd Annual ACM Symposium on Theory of Computing (STOC)}, pp.~151--158, 1971.
  \bibitem{turing} A.~M.~Turing, ``On Computable Numbers, with an Application to the Entscheidungsproblem,'' \emph{Proc.\ London Mathematical Society}, Ser.~2, Vol.~42, pp.~230--265, 1936.
\end{thebibliography}

\end{document}