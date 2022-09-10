type TrieNode struct {
	child map[byte]*TrieNode
	isWord bool
}

func newTrieNode() *TrieNode {
	return &TrieNode{
		child: make(map[byte]*TrieNode),
		isWord: false,
	}
}

type Trie struct {
    root *TrieNode
}


func Constructor() Trie {
    return Trie{
		root: newTrieNode(),
	}
}


func (this *Trie) Insert(word string)  {
    curr := this.root

	for i:= range word{
		if _, ok := curr.child[word[i]]; !ok {
			curr.child[word[i]] = newTrieNode()
		}
		curr = curr.child[word[i]]
	}
	curr.isWord = true
}


func (this *Trie) Search(word string) bool {
    curr := this.root
	for i:= range word{
		if _, ok := curr.child[word[i]]; !ok{
			return false
		}
		curr = curr.child[word[i]]
	}
	return curr.isWord
}


func (this *Trie) StartsWith(prefix string) bool {
	curr := this.root
	for i:= range prefix{
		if _, ok := curr.child[prefix[i]]; !ok{
			return false
		}
		curr = curr.child[prefix[i]]
	}
	return true
}