# 第2章：Pyの成分：数値・文字列・変数

### [TopPageに戻る](../README.md)

## 概要

1. 単純な組み込みデータ型を学ぶこと

- ブール値：TrueまたはFalseの値を持つ
- 整数：数値＜1，200，300000など＞
- 浮動小数点数：小数点以下の部分がある数値，(1.0e8)
- 文字列：文字の並び

Pythonでは，全てがオブジェクトとして実装されている．
オブジェクトには，ブール値，整数などのデータ型があり，そのデータで何ができるかは，型によって決まる．型は「ミュータブル：データの値を変更できる」「イミュータブル：変更できない」．Pythonは，強く型付けされている．これは，値がミュータブルでも，オブジェクトの型はわからない．
変数はただの名前であり，データを入れているオブジェクトに名前をつけているだけ．
Pythonでは，クラスと型は全く同じ意味になる．

- 計算式
<table>
	<thead>
    <tr>
      <th>計算式</th>
			<th>内容</th>
			<th>例</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>+</td>
      <td>足し算</td>
			<td><code class="python-code">1+3</code></td>
    </tr>
		<tr>
      <td>-</td>
      <td>引き算</td>
			<td><code class="python-code">1-3</code></td>
    </tr>
		<tr>
      <td>*</td>
      <td>掛け算</td>
			<td><code class="python-code">2*3</code></td>
    </tr>
		<tr>
      <td>/</td>
      <td>割り算</td>
			<td><code class="python-code">9/5</code></td>
    </tr>
		<tr>
      <td>//</td>
      <td>割り算後に，商を出力</td>
			<td><code class="python-code">9//5</code></td>
    </tr>
		<tr>
      <td>%</td>
      <td>割り算後に，剰余を出力</td>
			<td><code class="python-code">9%5</code></td>
    </tr>
		<tr>
      <td>divmod</td>
      <td>割り算の商とあまりをタプルで返す</td>
			<td><code class="python-code">divmod(9,5)</code></td>
    </tr>
  </tbody>
</table>

### 基数
<table>
	<thead>
    <tr>
      <th>基数</th>
			<th>内容</th>
			<th>例</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0b または 0B</td>
      <td>2進数</td>
			<td><code class="python-code">0b101</code></td>
    </tr>
		<tr>
      <td>0o または 0O</td>
      <td>8進数</td>
			<td><code class="python-code">0o1234567</code></td>
    </tr>
		<tr>
      <td>0x または 0X</td>
      <td>16進数</td>
			<td><code class="python-code">0x12abc</code></td>
    </tr>
  </tbody>
</table>

### 文字列
Pythonシーケンスの最初の例になる．Pythonの文字列はいミュータブルである．
- 「''」：文字列
- 「""」：文字列
- 「'''  '''」「"""  """」：複数行文字列
- 「\」によるエスケープ：他の方法では，表現しにくいものを表現できる．「\n」で改行など
- 「+」による連結：文字列を連結できる
- 「[]」：による文字の抽出：文字列の中の一つの文字を取り出したいときには，文字列名後ろに角カッコで囲んだ文字のオフセットを続ける．先頭の文字オフセットは，「0」．末尾のオフセットは「-1」で指定できる．
- 文字列はイミュータブルなので，文字列に直接文字を挿入したり，指定したインデックスの位置の文字を書き換えたりすることはできない．
- [start:end:step]：スライスを使えば，文字列から部分文字列を取り出すことができる．先頭オフセット(start)，末尾オフセット(end)，ステップで定義する．<br>
	[:]は先頭から末尾までのシーケンス全体を抽出する [start:]は指定したところから末尾まで [:end]は先頭からend-1までのシーケンスを抽出 [start:end:step]はstep文字ごとにstartからend-1までのシーケンスを抽出
- 「len()」：len()関数は，文字列内の文字数を数える
- 「split()」：split()関数は，splitを使えば，セパレータに基づいて文字列を分割し，部分文字列のリストを作ることができる．splitの引数なしは，空白文字のシーケンスを使うようになっている．
- 「join()」：結合．文字列のリストを一つの文字列に結合する．string.join(list)という形式で書ける．stringには，繋げる時に使う文字列を決める．
- 「startswith()」：先頭が指定した引数になっているか？
- 「endswith()」：末尾が指定した引数になっているか？
- 「find()」：文字列の中に最初に引数の文字があれば，それのオフセットを返す
- 「rfind()」：最後にある文字のオフセットを返す
- 「count()」：引数の文字の出現回数
- 「isalnum()」：文字はすべて英字か数字になっているか？
- 「strip()」：指定した文字を取り除く
- 「capitalize()」：先頭の単語をタイトルケースにする
- 「tutle()」：すべての単語をタイトルケースにする
- 「upper()」：すべての文字を大文字にする
- 「lower()」：すべての文字を小文字にする
- 「swapcase()」：大文字を小文字を逆にする
- 「center()」：数字の引数を与えて，それに合うように中央にする
- 「ljust()」：左端
- 「rjust()」：右端
- 「replace()」：部分文字列を簡単に書き換えられる．書き換え前後の部分文字列と書き換えの回数を指定する．最後の回数を省略すると置換はすべての場所で行われる．

### 型変換
<table>
	<thead>
    <tr>
      <th>変換指定方法</th>
			<th>内容</th>
			<th>例</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>int</td>
      <td>整数型</td>
			<td><code class="python-code">int(129.123)</code></td>
    </tr>
		<tr>
      <td>float</td>
      <td>浮動小数点</td>
			<td><code class="python-code">float(123.123)</code></td>
    </tr>
		<tr>
      <td>str</td>
      <td>文字列</td>
			<td><code class="python-code">str(78.8)</code></td>
    </tr>
  </tbody>
</table>