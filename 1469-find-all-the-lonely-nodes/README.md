<h2><a href="https://leetcode.com/problems/find-all-the-lonely-nodes/">1469. Find All The Lonely Nodes</a></h2><h3>Easy</h3><hr><div><p>In a binary tree, a <strong>lonely</strong> node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.</p>

<p>Given the <code>root</code> of a binary tree, return <em>an array containing the values of all lonely nodes</em> in the tree. Return the list <strong>in any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/03/e1.png" style="width: 203px; height: 202px;">
<pre><strong>Input:</strong> root = [1,2,3,null,4]
<strong>Output:</strong> [4]
<strong>Explanation:</strong> Light blue node is the only lonely node.
Node 1 is the root and is not lonely.
Nodes 2 and 3 have the same parent and are not lonely.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/03/e2.png" style="width: 442px; height: 282px;">
<pre><strong>Input:</strong> root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
<strong>Output:</strong> [6,2]
<strong>Explanation:</strong> Light blue nodes are lonely nodes.
Please remember that order doesn't matter, [2,6] is also an acceptable answer.
</pre>

<p><strong>Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/03/tree.png" style="width: 363px; height: 202px;">
<pre><strong>
Input:</strong> root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
<strong>Output:</strong> [77,55,33,66,44,22]
<strong>Explanation:</strong> Nodes 99 and 88 share the same parent. Node 11 is the root.
All other nodes are lonely.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the <code>tree</code> is in the range <code>[1, 1000].</code></li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>6</sup></code></li>
</ul>
</div>