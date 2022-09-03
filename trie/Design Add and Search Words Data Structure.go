type TrieNode struct {
    children [26]*TrieNode
    is_word bool
}

type WordDictionary struct {
    root *TrieNode
}


func Constructor() WordDictionary {
    return WordDictionary{
        root: &TrieNode{},
    }
}


func (this *WordDictionary) AddWord(word string)  {
    cur := this.root
    for i:= range word{
        if cur.children[word[i] - 'a'] == nil{
            cur.children[word[i] - 'a'] = &TrieNode{}          
        }
        cur = cur.children[word[i] - 'a']
    }
    cur.is_word = true
}


func (this *WordDictionary) Search(word string) bool {
    return this.helperSearch(word, this.root)
}


func (this *WordDictionary) helperSearch(word string, node *TrieNode) bool {
    if node == nil{
        return false
    }
    curr:= node
    for i:= range word{
        if word[i] == '.'{
            for j:=0;j<26;j++{
                if this.helperSearch(word[i+1:], curr.children[j]) {
                    return true
                }
            }
            return false
        } else {
            if curr.children[word[i]-'a'] == nil{
                return false
            }
            curr = curr.children[word[i]-'a']
        }
    }
    return curr.is_word
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */