<template>
  <div class="db-flex-column db-bordered db-flex-item-half">

    <div class="db-flex-item-2 db-flex-row db-bottom-border">
      <div class="db-padding-horizontal db-flex-item db-align-vertical-center">
        <h6><span class="emoji" v-if="emoji">{{ emoji }}</span>&nbsp;{{ name }}&nbsp;</h6>
        <em v-for="(speaker, index) in speakers">
          <span v-if="index !== 0">, </span>{{ speaker }}
        </em>
      </div>
      <div class="db-padding-horizontal db-flex-static "></div>
    </div>

    <div class="db-flex-item-2 db-flex-row db-bottom-border"><!-- Keys -->
      <div class="db-align-vertical-center  db-left-text" :class="{ 'db-flex-item-fws': !roundInfo.positions.length > 2, 'db-flex-item-fwm': roundInfo.positions.length > 2 }">
      </div>
      <div v-if="roundInfo.showPronouns" class="db-align-vertical-center db-align-horizontal-center db-flex-item-fwl">
        <em>Pronoun</em>
      </div>
      <div class="db-align-vertical-center db-padding-horizontal db-align-horizontal-center db-flex-item">
        <em>First and Last Name</em>
      </div>
      <div class="db-align-vertical-center db-flex-item-fwl db-align-horizontal-center">
        <em>Score</em>
      </div>
    </div>

    <div class="db-flex-item-2 db-flex-row" v-for="x in roundInfo.speakersCount"><!-- Speakers -->
      <div class="db-align-vertical-center db-right-text db-flex-item-fws">
        {{ x }}
      </div>
      <div v-if="roundInfo.showPronouns" class="db-fill-in db-flex-item-fwl"></div>
      <div class="db-padding-horizontal db-fill-in db-flex-item"></div>
      <div class="db-padding-horizontal db-fill-in db-flex-item-fwl"></div>
    </div>

    <div class="db-flex-item-2 db-flex-row db-bottom-border" v-if="roundInfo.hasReplies"><!-- Replies -->
      <div class="db-align-vertical-center db-right-text db-flex-item-fws">
        R
      </div>
      <div class="db-fill-in db-flex-item-fwl"></div>
      <div class="db-padding-horizontal db-fill-in db-flex-item"></div>
      <div class="db-padding-horizontal db-fill-in db-flex-item-fwl"></div>
    </div>

    <div class="db-flex-item-2 db-flex-row"><!-- Totals -->
      <div class="db-align-vertical-center  db-left-text db-padding-horizontal db-flex-item-fws"></div>
      <div class="db-flex-item db-flex-row db-align-vertical-center"></div>
      <div class="db-padding-horizontal db-static db-align-vertical-center db-right-text">
        {{ position }}'s Total Score:
      </div>
      <div class="db-fill-in db-flex-item-fwl"></div>
    </div>

  </div>
</template>

<script>
export default {
  props: {
    name: String,
    emoji: String,
    speakers: Array,
    position: String,
    roundInfo: Object
  },
}
</script>
