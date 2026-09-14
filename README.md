# Minimal Lab Project

Generated student documentation belongs in the starter project.

# Minimal Lab Project

This fixture demonstrates the version-1 authoring contract for startergen.

## Forward motion

The exercise source is available here:

[Unicycle dynamics — UnicycleDynamics.f (src/lab_project/dynamics/unicycle.py:7-8)](src/lab_project/dynamics/unicycle.py#L7-L8)

> **Note — Learning goal**
> Keep the implementation readable and test the forward-motion case.

Inline math uses $v = r\omega$ and a matrix example follows:

$$
\begin{bmatrix} x \\ y \end{bmatrix}
=
\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}.
$$

![A small lab diagram](assets/lab-diagram.svg)

```text
{{ exercise("unicycle-dynamics") }}
```
